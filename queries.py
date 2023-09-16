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

create_comment_query = """
    mutation upsertComment($text: String!, $parentId: ID!) {
        upsertComment(text: $text, parentId: $parentId) {
            id
        }
    }
"""

upsert_link_query = """
mutation ($id: ID, $sub: String, $title: String!, $url: String!, $boost: Int, $forward: [ItemForwardInput], $hash: String, $hmac: String) {
    upsertLink(id: $id, sub: $sub, title: $title, url: $url, boost: $boost, forward: $forward, hash: $hash, hmac: $hmac) {
        id
    }
}
"""

upsert_bounty_query = """
mutation ($title: String!, $text: String, $bounty: Int, $id: ID, $sub: String, $boost: Int, $forward: [ItemForwardInput], $hash: String, $hmac: String) {
    upsertBounty(title: $title, text: $text, bounty: $bounty, id: $id, sub: $sub, boost: $boost, forward: $forward, hash: $hash, hmac: $hmac) {
        id
    }
}
"""

upsert_job_query = """
mutation ($sub: String!, $title: String!, $company: String!, $text: String!, $url: String!, $maxBid: Int!, $id: ID, $location: String, $remote: Boolean, $status: String, $logo: Int, $hash: String, $hmac: String) {
    upsertJob(sub: $sub, title: $title, company: $company, text: $text, url: $url, maxBid: $maxBid, id: $id, location: $location, remote: $remote, status: $status, logo: $logo, hash: $hash, hmac: $hmac) {
        id
    }
}
"""

upsert_poll_query = """
mutation ($title: String!, $options: [String!]!, $id: ID, $sub: String, $text: String, $boost: Int, $forward: [ItemForwardInput], $hash: String, $hmac: String) {
    upsertPoll(title: $title, options: $options, id: $id, sub: $sub, text: $text, boost: $boost, forward: $forward, hash: $hash, hmac: $hmac) {
        id
    }
}
"""

upsert_discussion_query = """
mutation ($title: String!, $id: ID, $sub: String, $text: String, $boost: Int, $forward: [ItemForwardInput], $hash: String, $hmac: String) {
    upsertDiscussion(title: $title, id: $id, sub: $sub, text: $text, boost: $boost, forward: $forward, hash: $hash, hmac: $hmac) {
        id
    }
}
"""
