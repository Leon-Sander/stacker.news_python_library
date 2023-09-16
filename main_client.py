
from retrying import retry
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from config import ENDPOINT
from logger import logger
from authentication_manager import AuthenticationManager
from item_manager import ItemManager
from notification_manager import NotificationManager
from push_subscription_manager import PushSubscriptionManager
import os
from dotenv import load_dotenv
load_dotenv()

class StackerNewsGraphQL:

    def __init__(self, endpoint=ENDPOINT):
        headers = {
            'Content-Type': 'application/json',
            'Cookie': os.getenv("SN_AUTH_COOKIE")  # Set the Cookie header
        }
        transport = AIOHTTPTransport(url=endpoint, headers=headers)
        self.client = Client(transport=transport, fetch_schema_from_transport=False)


        self.authentication_manager = AuthenticationManager(self.client)
        self.item_manager = ItemManager(self.client)
        self.notification_manager = NotificationManager(self.client)
        self.push_subscription_manager = PushSubscriptionManager(self.client)

    def refresh_session(self):
        return self.authentication_manager.refresh_session()
    
    def get_current_session(self):
        return self.authentication_manager.get_current_session()

    def get_items(self, limit=10, cursor=None, sort="NEW", type=None, sub=None, name=None, when=None, by=None):
        return self.item_manager.get_items(limit, cursor, sort, type, sub, name, when, by)

    def search_items(self, q, sub=None, cursor=None, what=None, sort=None, when=None, limit=10):
        return self.item_manager.search_items(q, sub, cursor, what, sort, when, limit)

    def get_item_by_id(self, item_id):
        return self.item_manager.get_item_by_id(item_id)



    def check_duplicate(self, url):
        return self.item_manager.check_duplicate(url)

    def get_rss_url(self, tag=None):
        return self.item_manager.get_rss_url(tag)
    
    def has_new_notifications(self):
        return self.notification_manager.has_new_notifications()

    def get_notifications(self, cursor=None, inc=None):
        return self.notification_manager.get_notifications(cursor, inc)

    def delete_push_subscription(self, endpoint):
        return self.push_subscription_manager.delete_push_subscription(endpoint)

    def save_push_subscription(self, endpoint, p256dh, auth, old_endpoint=None):
        return self.push_subscription_manager.save_push_subscription(endpoint, p256dh, auth, old_endpoint)
