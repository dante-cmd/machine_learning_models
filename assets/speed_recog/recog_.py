from speech_recognition import Recognizer, Microphone, UnknownValueError
#import pyttsx3
from gtts import gTTS
import playsound
import pyaudio
import re


def speak(text):
    tss = gTTS(text=text, lang='es')
    file_name = 'voice.mp3'
    tss.save(file_name)
    playsound.playsound(fr'C:\Users\Dante\Desktop\python-course\datascience\machine_learning_models\{file_name}')

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

names_gmail = {'Richard':'richard@data_science.com', 'taza':'lataza.123@gmail.com'}


import time

total_seconds = 30
count_second = 0
start = time.time()

recognizer = Recognizer()


while total_seconds>count_second:
    
    # current_time = time.time()
    # count_second = current_time - start
    # print('---------------------', count_second)
    
    try:
        
            
        with Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic ) #, duration = 1)
            audio  =recognizer.listen(mic)
            text = recognizer.recognize_google(audio, language='es-ES')
            text = text.lower()
            print(text)
            

            #current_time = time.time()
            #print(current_time, '--------------')
            
            
            #print(text)
            
            if re.search(r'.*(?:enviar|mandar).*mensaje.*', text):

                speak('A quién deseas enviar el mensaje?')

            elif re.search(r'.*a.*\s([a-z]+).*', text): # and re.search(r'.*(ri(?:c|s)har(?:d|).*', text, re.I):
                speak('Por Whatsapp or Gmail?')
                #print(5000)

                name_of_user = re.search(r'.*a.*\s([a-z]+).*', text, re.I).group(1)
                
                print(name_of_user)
                # condition = False
                

                us_gmail = [names_gmail[an] for an in names_gmail if similar(an, name_of_user)>=0.85][0]
                print(us_gmail)

                # if names_gmail.keys()
                # name_of_user
                # condition = False
                
            # elif re.search(r'.*por.*(?:wha.*|gma.*).*', text):

            #     speak(rf'Se está enviando a {us_gmail}')
            #     

               #audio  =recognizer.listen(mic)
               #text = recognizer.recognize_google(audio, language='es-ES')
               #text = text.lower()

               #speak('Se enviará un mensaje pronto')

                #print(f'Recognize {text}')
    except:
        break
        #pass

# https://github.com/mozilla/DeepSpeech-examples