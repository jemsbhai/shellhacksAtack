import requests
import sys
import json

url = "http://shellhacks2018-env.bcusih3bg3.us-east-1.elasticbeanstalk.com/media"

##payload = "{ \"url\": \"https://storage.googleapis.com/shellhacks/chris.jpg\",\n  \"type\": \"image\",\n  \"reportId\": \"5b9df59e93c9137ee6ec6283\"\n\t\n}"


load = {
     "url" : sys.argv[1],
     "type": sys.argv[2],
     "reportId": sys.argv[3]
     
}

payload = json.dumps(load)


headers = {
    'Content-Type': "application/json",
    'Authorization': "48e10f6282dfa0055f4318ae8cf73b4bc4e2345fa2c5f8d5137edc43b308048ebdc6910730f6bff2278966b662382fbf5db72f50ba4408b28f63571fdf5862a5f1e78b06b689c11262e3777944b2ef1f816d03172586bf3b3e37a89192f0e4a071bea8950ef970f9128d19a25d7969c986c391cda88ae377bc3d17363da190b46d5f4915e1a8e2bdaab374b5d9d64bb0523f1fba3ef5746e13445a50fbac48fa2945972fcf4203a3b145a60b3a33ca0f74051467ef80b92f5d3c231ea50f302ab6cf60e5767b04fa3f15a68f3ad9e7cd0bf74d6c33b3ec99011fd0128d168e98271b43d8e7dc47a134311c051e6f088ef10e7b6be67efe681483745719c0d0fc",
    'Cache-Control': "no-cache",
    'Postman-Token': "268ba33c-db4b-4f3b-a135-bd408cd3649a"
    }

response = requests.request("POST", url, data=payload, headers=headers)

##print(response.text)

parsed = json.loads(response.text)

print (parsed["mediaId"])


