


# StackerNews GraphQL API Wrapper
## This code is under development, many functions might not work, I will fix it in the coming days and weeks.
This Python module provides a wrapper around the StackerNews GraphQL API. It handles the basic operations such as logging in, fetching items, searching, and other functionalities provided by the API.



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

1. **Login**:
   - Parameters:
     - `k1`: A string representing the k1 key for authentication.
     - `sig`: A string representing the signature for authentication.
   ```python
   sn.login(k1="your_k1", sig="your_sig")
   ```

2. **Logout**:
   ```python
   sn.logout()
   ```

3. **Token Validation**:
   Check if the current JWT token is valid:
   ```python
   is_valid = sn.validate_token()
   ```

### Fetching Data

1. **Get Items**:
   Retrieve a list of items based on the provided parameters.
   ```python
   items = sn.get_items(limit=10, sort="NEW")
   ```

2. **Search Items**:
   Search for items based on the given query string and other optional parameters.
   ```python
   search_results = sn.search_items(q="python")
   ```

3. **Get Item by ID**:
   Retrieve a specific item by its ID.
   ```python
   item = sn.get_item_by_id(item_id=12345)
   ```

4. **Get Current Session**:
   Retrieve details about the current logged-in user/session.
   ```python
   session_info = sn.get_current_session()
   ```

5. **Get Notes**:
   Retrieve a list of notes.
   ```python
   notes = sn.get_notes(limit=10)
   ```

6. **Check for Duplicate Items**:
   Check if an item with the given URL already exists.
   ```python
   duplicates = sn.check_duplicate(url="https://example.com")
   ```

7. **Get RSS URL**:
   Retrieve the RSS URL for the provided tag (optional).
   ```python
   rss_url = sn.get_rss_url(tag="python")
   ```

