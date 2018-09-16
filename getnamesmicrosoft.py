import requests
import sys
import json

url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"

##payload = "{\r\n        \"documents\": [\r\n            {\r\n                \"language\": \"en\",\r\n                \"id\": \"1\",\r\n                \"text\": \"We love this trail and make the trip every year. The views are breathtaking and well worth the hike!\"\r\n            },\r\n            {\r\n                \"language\": \"en\",\r\n                \"id\": \"2\",\r\n                \"text\": \"Poorly marked trails! I thought we were goners. Worst hike ever.\"\r\n            }\r\n        ]\r\n    }"

load = {}

load['documents'] = []

load['documents'].append({
    "language": "en",
    "id": "1",
    "text": sys.argv[1]
    })

payload = json.dumps(load)

headers = {
    'Ocp-Apim-Subscription-Key': "53660e609994450a82dfffa38d8820f3",
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "9b95f2fa-8e4e-4e07-bf91-f60118f6b3d0"
    }

response = requests.request("POST", url, data=payload, headers=headers)

##print(response.text)

parsed = json.loads(response.text)

##print (parsed["documents"][0]["score"])

for word in parsed["documents"][0]["keyPhrases"] :
    ##print (word)
    if word[0].isupper():
        print (word)
        break
