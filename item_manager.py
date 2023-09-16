
from retrying import retry
from gql import gql
from logger import logger
from queries import upsert_discussion_query, upsert_poll_query, upsert_job_query, upsert_bounty_query, upsert_link_query, get_items_query, search_items_query, get_item_by_id_query, check_duplicate_query, create_comment_query

class ItemManager:
    def __init__(self, client):
        self.client = client

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


    def create_comment(self, parent_id, text):
        variables = {
            "text": text,
            "parentId": parent_id
        }
        response = self.execute(create_comment_query, variables)
        return response["upsertComment"]["id"]

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

    def upsert_link(self, title, url, sub=None, id=None, boost=None, forward=None, hash=None, hmac=None):
        variables = {
            "title": title,
            "url": url,
            "sub": sub,
            "id": id,
            "boost": boost,
            "forward": forward,
            "hash": hash,
            "hmac": hmac
        }
        response = self.execute(upsert_link_query, variables)
        return response["upsertLink"]

    def upsert_bounty(self, title, text, bounty, id=None, sub=None, boost=None, forward=None, hash=None, hmac=None):
        variables = {
            "title": title,
            "text": text,
            "bounty": bounty,
            "id": id,
            "sub": sub,
            "boost": boost,
            "forward": forward,
            "hash": hash,
            "hmac": hmac
        }
        response = self.execute(upsert_bounty_query, variables)
        return response["upsertBounty"]

    def upsert_job(self, sub, title, company, text, url, maxBid, id=None, location=None, remote=None, status=None, logo=None, hash=None, hmac=None):
        variables = {
            "sub": sub,
            "title": title,
            "company": company,
            "text": text,
            "url": url,
            "maxBid": maxBid,
            "id": id,
            "location": location,
            "remote": remote,
            "status": status,
            "logo": logo,
            "hash": hash,
            "hmac": hmac
        }
        response = self.execute(upsert_job_query, variables)
        return response["upsertJob"]

    def upsert_poll(self, title, options, id=None, sub=None, text=None, boost=None, forward=None, hash=None, hmac=None):
        variables = {
            "title": title,
            "options": options,
            "id": id,
            "sub": sub,
            "text": text,
            "boost": boost,
            "forward": forward,
            "hash": hash,
            "hmac": hmac
        }
        response = self.execute(upsert_poll_query, variables)
        return response["upsertPoll"]

    def upsert_discussion(self, title, id=None, sub=None, text=None, boost=None, forward=None, hash=None, hmac=None):
        variables = {
            "title": title,
            "id": id,
            "sub": sub,
            "text": text,
            "boost": boost,
            "forward": forward,
            "hash": hash,
            "hmac": hmac
        }
        response = self.execute(upsert_discussion_query, variables)
        return response["upsertDiscussion"]
