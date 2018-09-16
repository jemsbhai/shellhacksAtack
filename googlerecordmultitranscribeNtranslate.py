import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import translate

import sys

if len(sys.argv) < 2:
    print ('incorrect number of arguments')
    sys.exit()

print (sys.argv[1])

inputfilename = sys.argv[1]

commandstring = "arecord " + inputfilename + " -f S16_LE -r 16000 -d 7"

os.system(commandstring)

# Instantiates a client
##client = speech.SpeechClient()

client = speech.SpeechClient.from_service_account_json('pennapps-fit.json')

##translate_client = translate.Client()

translate_client = translate.Client.from_service_account_json('pennapps-fit.json')

#translate whatever is found to english
target = 'en' 

# The name of the audio file to transcribe
file_name = os.path.join( os.path.dirname(__file__),sys.argv[1])

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    text = result.alternatives[0].transcript
    with open('transcript.txt', 'w') as the_file:
        the_file.write(text)


##    text = result.alternatives[0].transcript
    translation = translate_client.translate(text, target_language=target)
    print(u'Translation: {}'.format(translation['translatedText']))
    with open('translation.txt', 'w') as the_file2:
        the_file2.write(translation['translatedText'])



