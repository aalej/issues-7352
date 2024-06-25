import requests

emulator_url = 'http://127.0.0.1:50579/v1/projects/test-app:runQuery'

payload = b'{"partitionId": {"projectId": "test-app", "namespaceId": ""}, "query": {"kind": [{"name": "Profile"}], "limit": 1}, "readOptions": {"readConsistency": "EVENTUAL"}}'

headers = {'Content-Length': '169', 'Content-Type': 'application/json'}

# POST request to the emulator
resp = requests.post(emulator_url, headers=headers, data=payload)

# check response's data
data = resp.json()
print(data)
# prints {'batch': {'entityResultType': 'FULL', 'moreResults': 'MORE_RESULTS_AFTER_LIMIT', 'readTime': '2024-06-21T20:20:20.928406Z'}} no "endCursor" within the data.