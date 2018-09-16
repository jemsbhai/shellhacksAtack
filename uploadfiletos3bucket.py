import boto3
import json
import time
import sys


if len(sys.argv) < 3:
    print ('incorrect number of arguments')
    sys.exit()


s3 = boto3.resource('s3')

filename1 = sys.argv[1]
filename2 = sys.argv[2]


sF1=filename1
d1 = open(sF1, 'rb')
sF2=filename2
s3.Bucket('shellhacks2018').put_object(ACL='public-read', Key=sF2, Body=d1)

