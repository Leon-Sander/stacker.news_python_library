from retrying import retry
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import jwt
from config import ENDPOINT
from logger import logger
from queries import *

class StackerNewsGraphQL:

    def __init__(self, endpoint=ENDPOINT):
        self.token = None  # Initialize the token attribute
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        transport = AIOHTTPTransport(url=endpoint, headers=headers)
        self.client = Client(transport=transport, fetch_schema_from_transport=False)

    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=3)
    def execute(self, query, variables=None):
        gql_query = gql(query)
        try:
            return self.client.execute(gql_query, variable_values=variables)
        except Exception as e:
            logger.error(f"Error executing query: {str(e)}")
            raise

    async def execute_async(self, query, variables=None):
        gql_query = gql(query)
        try:
            return await self.client.execute_async(gql_query, variable_values=variables)
        except Exception as e:
            logger.error(f"Error executing query: {str(e)}")
            raise



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

    def get_items(self, limit=10, cursor=None, sort="NEW", type=None, sub=None, name=None, when=None, by=None):
        variables = {
            "limit": limit,
            "cursor": cursor,
            "sort": sort,
            "type": type,
            "sub": sub,
            "name": name,
            "when": when,
            "by": by
        }
        response = self.execute(get_items_query, variables)
        return {
            "items": response["items"],
            "cursor": cursor,
            "limit": limit
        }

    def search_items(self, q, sub=None, cursor=None, what=None, sort=None, when=None, limit=10):
        variables = {
            "q": q,
            "sub": sub,
            "cursor": cursor,
            "what": what,
            "sort": sort,
            "when": when
        }
        response = self.execute(search_items_query, variables)
        return response['search']['items']

    def get_item_by_id(self, item_id):
        variables = {
            "id": item_id
        }
        return self.execute(get_item_by_id_query, variables)

    def get_current_session(self):
        return self.execute(get_current_session_query)

    def get_notes(self, limit=10, skip=0):
        variables = {
            "limit": limit,
            "skip": skip
        }
        return self.execute(get_notes_query, variables)

    def check_duplicate(self, url):
        variables = {
            "url": url
        }
        return self.execute(check_duplicate_query, variables)

    def get_rss_url(self, tag=None):
        variables = {"tag": tag} if tag else {}
        return self.execute(get_rss_url_query, variables)