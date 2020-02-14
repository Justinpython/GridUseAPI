import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get('https://api.carbonintensity.org.uk/regional/scotland', params={})

data = response.json()

jprint(data)
