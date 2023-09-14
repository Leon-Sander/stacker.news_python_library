from main_client import StackerNewsGraphQL
client = StackerNewsGraphQL(endpoint="https://stacker.news/api/graphql")
output = client.get_items(limit=2, sort="TOP")
print(output)