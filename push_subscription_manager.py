
from retrying import retry
from gql import gql
from logger import logger

class PushSubscriptionManager:
    def __init__(self, client):
        self.client = client

    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=3)
    def execute(self, query, variables=None):
        gql_query = gql(query)
        try:
            return self.client.execute(gql_query, variable_values=variables)
        except Exception as e:
            logger.error(f"Error executing query: {str(e)}")
            raise
    
    def delete_push_subscription(self, endpoint):
        mutation = '''
        mutation($endpoint: String!) {
        deletePushSubscription(endpoint: $endpoint) {
            id
            userId
            endpoint
            p256dh
            auth
        }
        }
        '''
        variables = {
            "endpoint": endpoint
        }
        return self.execute(mutation, variables)

    def save_push_subscription(self, endpoint, p256dh, auth, old_endpoint=None):
        mutation = '''
        mutation($endpoint: String!, $p256dh: String!, $auth: String!, $oldEndpoint: String) {
        savePushSubscription(endpoint: $endpoint, p256dh: $p256dh, auth: $auth, oldEndpoint: $oldEndpoint) {
            id
            userId
            endpoint
            p256dh
            auth
        }
        }
        '''
        variables = {
            "endpoint": endpoint,
            "p256dh": p256dh,
            "auth": auth,
            "oldEndpoint": old_endpoint
        }
        return self.execute(mutation, variables)
