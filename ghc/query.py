# flake8: noqa

SEARCH_REPOSITORY = '''
query($search_query_str:String!, $end_cursor:String) {
    search(type: REPOSITORY, first: 100, query: $search_query_str, after: $end_cursor) {
        repositoryCount
        edges {
            node {
                ... on Repository {
                    name
                    description
                    isArchived
                    isTemplate
                    url
                    primaryLanguage {
                        name
                    }
                }
            }
        }
        pageInfo {
            endCursor
            hasNextPage
        }
    }
}
'''
