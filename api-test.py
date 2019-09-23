import requests

url = 'http://history.muffinlabs.com/date'

r = requests.get(url)

json_output = r.json()

print(json_output)


data = json_output['data']

events = data['Events']

for event in events:
    print(event['text'])
