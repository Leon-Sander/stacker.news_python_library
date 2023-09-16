
from retrying import retry
from gql import gql
from logger import logger
from queries import get_items_query, search_items_query, get_item_by_id_query, check_duplicate_query, get_rss_url_query

class ItemManager:
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

    def check_duplicate(self, url):
        variables = {
            "url": url
        }
        return self.execute(check_duplicate_query, variables)
