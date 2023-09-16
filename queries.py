# Login mutation
login_mutation = """
    mutation ($k1: String!, $sig: String!) {
        lnurlauth(k1: $k1, sig: $sig) {
            ok
            jwt
            error
        }
    }
"""

# Logout mutation
logout_mutation = """
    mutation {
        logout {
            ok
        }
    }
"""

# Get items query
get_items_query = """
    query ($limit: Int, $cursor: String, $sort: String, $type: String, $sub: String, $name: String, $when: String, $by: String) {
        items(limit: $limit, cursor: $cursor, sort: $sort, type: $type, sub: $sub, name: $name, when: $when, by: $by) {
            items {
                id
                createdAt
                updatedAt
                title
                url
                text
                user {
                    id
                }
                
                boost
                upvotes
                wvotes
                ncomments
            }
        }
    }
"""

# Search items query
search_items_query = """
    query ($q: String, $sub: String, $cursor: String, $what: String, $sort: String, $when: String) {
        search(q: $q, sub: $sub, cursor: $cursor, what: $what, sort: $sort, when: $when) {
            items {
                id
                title
                url
                text
                user {
                    id
                    name
                }
            }
        }
    }
"""

# Get item by ID query, depth removed
get_item_by_id_query = """
    query ($id: ID!) {
        item(id: $id) {
            id
            createdAt
            updatedAt
            title
            url
            text
            user {
                id
                name
            }
            
            boost
            bounty
            upvotes
            wvotes
            ncomments
        }
    }
"""

# Get current session query
get_current_session_query = """
    query {
        me {
            id
            name
            bio {
                title
                url
            }
        }
    }
"""

# Get notes query
get_notes_query = """
    query ($limit: Int, $skip: Int) {
        notes(limit: $limit, skip: $skip) {
            id
            text
            createdAt
            updatedAt
            user {
                id
                name
            }
        }
    }
"""

# Check duplicate query
check_duplicate_query = """
    query ($url: String!) {
        dupes(url: $url) {
            id
            title
            createdAt
        }
    }
"""

# Get RSS URL query
get_rss_url_query = """
    query ($tag: String) {
        rss(tag: $tag)
    }
"""
