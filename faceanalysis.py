import boto3
import json
import time
import sys

if len(sys.argv) < 2:
    print ('incorrect number of arguments')
    sys.exit()

s3 = boto3.resource('s3')

filename1 = sys.argv[1]

sF1=filename1
d1 = open(sF1, 'rb')
s3.Bucket('shellhacks2018').put_object(ACL='public-read', Key=sF1, Body=d1)

bucket='shellhacks2018'

client=boto3.client('rekognition')

response2 = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':filename1}},Attributes=['ALL'])

##print('Detected faces for ' + filename1)
for faceDetail in response2['FaceDetails']:
##    print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
##          + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
##    print('Here are the other attributes:')
##    print(json.dumps(faceDetail, indent=4, sort_keys=True))
    print (str(faceDetail['Gender']['Value']))
		   

		   
obj = s3.Object("shellhacks2018", filename1)
obj.delete()
