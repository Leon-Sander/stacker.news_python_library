


# StackerNews GraphQL API Wrapper

This Python library provides an interface to interact with the Stacker News GraphQL API. 

## Important

Some functions need authentication. Right now this is handled by pasting you session cookie into a .env file under SN_AUTH_COOKIE.
## How to Retrieve a Cookie from a Web Request:

   1. **Open Developer Tools**
      - Press `F12` on your keyboard to open your browser's developer tools when on the stacker.news website.

   2. **Navigate to the Network Tab**
      - In the developer tools panel, click on the `Network` tab.

   3. **Generate a Request**
      - If no requests are visible, interact with the web page (e.g., click a button or link) or simply refresh the page to generate new requests.

   4. **Select a Request**
      - In the `Network` tab, a list of requests will be shown. Click on any request from this list.

   5. **Access the Headers**
      - Once you've selected a request, details about that request will appear. Look for the `Headers` section.

   6. **Locate the Cookie**
      - Within the `Headers` section, scroll down until you find the `Cookie` header.
      - The value of the `Cookie` header will contain the desired cookie. You can select and copy this value for your use.


## Setup


1. Clone or download this repository to your local machine.

2. Install the necessary packages using pip:
   
   ```
   pip install -r requirements.txt
   ```

3. Import the `StackerNewsGraphQL` class from the module in your script:
   ```python
   from main_client import StackerNewsGraphQL
   ```

## Usage

### Initialization

Initialize the `StackerNewsGraphQL` class:

```python
sn = StackerNewsGraphQL()
```

### Authentication

- **refresh_session()**: Refreshes the user session.
- **get_current_session()**: Retrieves the details of the current user session.

### Items

- **get_items(limit, cursor, sort, type, sub, name, when, by)**: Fetches a list of items based on provided filters such as sorting, type, etc. Default limit is set to 10.
- **search_items(q, sub, cursor, what, sort, when, limit)**: Searches for items based on the given query string and other optional parameters. Default limit is set to 10.
- **get_item_by_id(item_id)**: Retrieves an item's details using its ID.
- **check_duplicate(url)**: Checks if a given URL has already been posted on Stacker News.
  
### Notifications

- **has_new_notifications()**: Checks if the user has any new notifications.
- **get_notifications(cursor, inc)**: Retrieves user notifications. Can be filtered using a cursor or inclusive flag.

### RSS Feed

- **fetch_rss_feed()**: Fetches the RSS feed from Stacker News. It will raise an error if the request is unsuccessful.

### Comments

- **create_comment(parent_id, text)**: Allows users to create a new comment under a specific parent item (e.g., post or another comment).

### TODO

- Implementing functions for creating new posts.
