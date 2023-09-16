
from retrying import retry
from gql import gql
from logger import logger

class NotificationManager:
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


    def has_new_notifications(self):
        query = '''
                {
                hasNewNotes
                }
                '''
        return self.execute(query)
    
    def get_notifications(self, cursor=None, inc=None):
        query = '''
        query($cursor: String, $inc: String) {
            notifications(cursor: $cursor, inc: $inc) {
                lastChecked
                cursor
                notifications {
                    ... on Reply {
                        id
                        item {
                            id
                            title
                        }
                        sortTime
                    }
                    ... on Votification {
                        id
                        earnedSats
                        item {
                            id
                            title
                        }
                        sortTime
                    }
                    # Add other notification types here.
                }
            }
        }
        '''
        variables = {
            "cursor": cursor,
            "inc": inc
        }
        return self.execute(query, variables)
