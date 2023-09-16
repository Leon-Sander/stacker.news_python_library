
from retrying import retry
from gql import gql
from logger import logger
from queries import login_mutation, logout_mutation, get_current_session_query
import jwt
from config import ENDPOINT
import os
import requests
from dotenv import load_dotenv
load_dotenv()

class AuthenticationManager:
    def __init__(self, client):
        self.client = client
        self.token = None  # Initialize the token attribute

    @retry(wait_exponential_multiplier=3000, wait_exponential_max=10000, stop_max_attempt_number=3, retry_on_exception=lambda e: True)
    def execute(self, query, variables=None, attempt=1):
        gql_query = gql(query)
        try:
            result = self.client.execute(gql_query, variable_values=variables)
            if attempt > 1:
                logger.info(f"Query succeeded on attempt {attempt}.")
            return result
        except Exception as e:
            logger.error(f"Error executing query on attempt {attempt}: {str(e)}")
            if attempt < 3:  # If it's not the last attempt
                return self.execute(query, variables, attempt + 1)
            raise


    def refresh_session(self):
        # Fetching the SN_AUTH_COOKIE from environment variables
        sn_auth_cookie = os.environ.get('SN_AUTH_COOKIE')

        if not sn_auth_cookie:
            raise ValueError("SN_AUTH_COOKIE not found in environment variables!")

        # Stacker News URL for refreshing the session
        sn_url = "https://stacker.news/api/auth/session" 

        # Preparing the request headers
        headers = {
            "Cookie": sn_auth_cookie
        }

        # Making the GET request to refresh the session
        response = requests.get(sn_url, headers=headers)
        
        # Handling the response
        if response.status_code != 200:
            raise Exception(f"Error refreshing SN session: {response.text}")

        return response.text  # or return True/None based on your preference
    
    def get_current_session(self):
        return self.execute(get_current_session_query)













    def login(self, k1, sig):
        variables = {
            "k1": k1,
            "sig": sig
        }
        response = self.execute(login_mutation, variables)
        if response.get("lnurlauth", {}).get("ok"):
            self.token = response["lnurlauth"]["jwt"]
            self._update_transport_with_token()
        else:
            raise Exception(response["lnurlauth"]["error"])
        return response

    def _update_transport_with_token(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        transport = AIOHTTPTransport(url=ENDPOINT, headers=headers)
        self.client = Client(transport=transport, fetch_schema_from_transport=False)

    def validate_token(self):
        if not self.token:
            return False
        try:
            decoded_token = jwt.decode(self.token, options={"verify_signature": False})
            return True
        except jwt.ExpiredSignatureError:
            return False

    def logout(self):
        return self.execute(logout_mutation)