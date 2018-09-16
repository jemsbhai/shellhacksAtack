# -*- coding: cp1252 -*-
import os
import sys
import time
import requests
import datetime
import subprocess



##light up LEDS to start
##os.system("node /home/pi/js-matrix-core-app/everloopred.js")

filename = time.strftime("%H-%M") + "_" + time.strftime("%d-%m-%Y")
audiofilename = filename + ".wav"
print (audiofilename)

picturefilename = filename +".jpg"

print (picturefilename)

print (datetime.datetime.now().isoformat())

datetimestamp = datetime.datetime.now().isoformat()

##take a picture

commandstring = "sudo raspistill -w 800 -h 600 -t 2 -o " + picturefilename
os.system(commandstring)



##record audio, upload and get transcript/translation

commandstring = "sudo python googlerecordmultitranscribeNtranslate.py " + audiofilename

os.system(commandstring)

transcribefilename = filename +"-raw.txt"
translatefilename = filename +"-translated.txt"

commandstring = "sudo mv transcript.txt " + transcribefilename
os.system(commandstring)
commandstring = "sudo mv translation.txt " + translatefilename
os.system(commandstring)

commandstring = "sudo python uploadfiletobucket.py shellhacksaudio " + audiofilename
os.system(commandstring)
commandstring = "sudo python uploadfiletobucket.py shellhackstext " + transcribefilename
os.system(commandstring)
commandstring = "sudo python uploadfiletobucket.py shellhackstext " + translatefilename
os.system(commandstring)
commandstring = "sudo python uploadfiletobucket.py shellhacks " + picturefilename
os.system(commandstring)




##check if we have a face that matches the reporter

commandstring = 'sudo python rekognize.py ' + picturefilename + " > result"
os.system(commandstring)

cmd = 'cat result'
name = subprocess.check_output(cmd, shell=True);
name = name.strip()

print ('recognition result: ' + name)

##if we dont have a name, lets anaylze the text to maybe find a name

file = open(translatefilename, "r") 
transtext =  file.read()
##print (transtext)

if "none" in name:
    cmd = 'sudo python getnamesmicrosoft.py "' + transtext + '"'
    n = subprocess.check_output(cmd, shell=True);
    if n[0].isupper():
        name = n
        ##add this new person to list of recognized people
        remotename = name +".jpg"
        commandstring = "sudo python uploadfiletos3bucket.py " + picturefilename + " " + remotename
        os.system(commandstring)

##if no name determined, default to unknown
if len(name) < 2:
    name = 'unknown'

##get some context

cmd = 'sudo python getconceptsmicrosoft.py "' + transtext +'"'
description = subprocess.check_output(cmd, shell=True);
description = description.strip()

if len(description) < 2:
    description = 'unknown'


print ('text context analysis result: ' + description)

##try to get the gender of the reporter
commandstring = "sudo python faceanalysis.py " + picturefilename + " > result2" 
os.system(commandstring)

cmd = 'cat result2'
gender = subprocess.check_output(cmd, shell=True);
gender = gender.strip()

if len(gender) < 2:
    gender = 'unknown'

print ('gender analysis result: ' + gender)
        
##generate a report
cmd = "sudo python generatereport.py " + name +" " + gender + " " + description + " " + datetimestamp 
reportid = subprocess.check_output(cmd, shell=True);

reportid = reportid.strip()
print(reportid)


##generate media records

cmd = "sudo python generatemediarecord.py https://storage.googleapis.com/shellhacks/" + picturefilename +" image " + reportid
mediaid = subprocess.check_output(cmd, shell=True);
print(mediaid)

cmd = "sudo python generatemediarecord.py https://storage.googleapis.com/shellhacksaudio/" + audiofilename +" audio " + reportid
mediaid = subprocess.check_output(cmd, shell=True);
print(mediaid)

cmd = "sudo python generatemediarecord.py https://storage.googleapis.com/shellhackstext/" + transcribefilename +" text " + reportid
mediaid = subprocess.check_output(cmd, shell=True);
print(mediaid)

cmd = "sudo python generatemediarecord.py https://storage.googleapis.com/shellhackstext/" + translatefilename +" text " + reportid
mediaid = subprocess.check_output(cmd, shell=True);
print(mediaid)





#clean up

commandstring = "sudo rm " + audiofilename
os.system (commandstring)

commandstring = "sudo rm " + picturefilename
os.system (commandstring)

commandstring = "sudo rm " + transcribefilename
os.system (commandstring)

commandstring = "sudo rm " + translatefilename
os.system (commandstring)

##light up LEDS to end
##os.system("node /home/pi/js-matrix-core-app/everloopblue.js")

