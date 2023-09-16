from main_client import StackerNewsGraphQL
client = StackerNewsGraphQL(endpoint="https://stacker.news/api/graphql")
# working:
#output = client.get_items(limit=2, sort="TOP")
#output = client.refresh_session()
#note_output = client.get_notifications()
#print(output)
print("##################################")
output = client.get_current_session()
print(output)