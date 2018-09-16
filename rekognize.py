import boto3
import json
import numpy as np
import time
import sys
##import cv2

##image capture and preprocess with opencv
##time.sleep(4)
##cap = cv2.VideoCapture(1)
##ret, img = cap.read()
##cv2.imwrite('capture.png',img)
##cap.release()
##time.sleep(4)




s3 = boto3.resource('s3')

infilename = sys.argv[1]


##for bucket in s3.buckets.all():
##    print(bucket.name)


bucket='shellhacks2018'
mybucket = s3.Bucket(bucket)
targetFiles = []
for object in mybucket.objects.all():
    ##print(object.key)
    targetFiles.append(object.key)

##name of the source file	
sourceFile=infilename

data = open(sourceFile, 'rb')
s3.Bucket('shellhacks2018').put_object(Key=sourceFile, Body=data)



##targetFile='peter.jpg'

##targetFiles = ['chris.jpg', 'peter.jpg']



client=boto3.client('rekognition')

found = 0
for target in targetFiles:

    response=client.compare_faces(SimilarityThreshold=85, SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}}, TargetImage={'S3Object':{'Bucket':bucket,'Name':target}})

    for faceMatch in response['FaceMatches']:
            position = faceMatch['Face']['BoundingBox']
            confidence = str(faceMatch['Face']['Confidence'])
##            print('The face at ' +
##                       str(position['Left']) + ' ' +
##                       str(position['Top']) +
##                       ' matches with ' + confidence + '% confidence')
##            print('\n recognized file is ' + target)
            ##print(json.dumps({"match": target, "confidence": confidence}, sort_keys=False))
            print(target[:-4])
            found = 1
            break
    if found==1:
        break


if found==0:
    ##print(json.dumps({"match": "none", "confidence": 0}, sort_keys=False))
    print('none')
  
		   

		   
obj = s3.Object("shellhacks2018", sourceFile)
obj.delete()
