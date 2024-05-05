# TODO: API Handling

import requests

ans = requests.get("https://api.freeapi.app/api/v1/public/randomjokes/joke/random")
data = ans.json()
if data['success']:
    print(data)

# The work here is to check Api