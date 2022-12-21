#main program
import speech_recognition as sr
import os
import re
import webbrowser
import requests
import pyttsx3
import datetime
import random
import math
from speedtest import Speedtest
from bs4 import BeautifulSoup
global k
k=True
global s
s=""
global q
q=0
def save():
    f=open("Commands.txt","w")
    f.write(s)
def t(str):
    global s
    engine = pyttsx3.init()
    print(str)
    engine.say(str)
    s=s+str+"\n"
    engine.runAndWait()
def st():
    st=Speedtest()
    d=str(int(st.download()/1000000))+"Mbps"
    u=str(int(st.upload()/1000000))+"Mbps"
    t("Download speed"+d)
    t("Upload speed"+u)
def cut():
    import shutil
    original = r'/home/adithyavardan/Desktop/newfolder/image'
    target = r'/home/adithyavardan/Desktop/new2folder'
    shutil.move(original, target)
def dt():
    x = datetime.datetime.now()
    t(x)
def cc():
    url="https://www.worldometers.info/coronavirus/"
    r=requests.get(url)
    s=BeautifulSoup(r.text,"html.parser")
    data=s.find_all("div",class_="maincounter-number")
    t("Total cases : "+str(data[0].text.strip()))
    t("Total deaths : "+str(data[1].text.strip()))
    t("Total Recovered : "+str(data[2].text.strip()))
def dice():
    x=random.randint(1,6)
    print("dice value = ")
    t(random.randint(1,6))
def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        t("Waiting for your responce")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        t('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError: 
        t('Your last command couldn\'t be heard')
        command = myCommand();
    return command
def assistant(command):
    "if statements for executing commands"
    if 'cut' in command:
        cut()
    elif 'speed test' in command:
        st()
    elif 'covid' in command:
        cc()
    elif 'date and time' in command:
        dt()
    elif 'dice' in command:
        dice()
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain+'.com'
            webbrowser.open(url)
            t("opening web browser")
        else:
            pass
    elif 'what\'s up' in command:
        
        t("just doing my thing")
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            
            t(str(res.json()['joke']))
        else:
            
            t("oops!I ran out of jokes")
    elif 'exit' in command:
        
        t("Have a great day")
        t("Do you want to save the file")
        command = myCommand()
        if 'yes' in command :
            save()
        elif 'no' in command:
            t("ok")
        t("Have a great day")
        exit()
    elif 'hai' in command:
        t("Are you seriously jobless!")
    else:
        
        t('I don\'t know what you mean!')

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
if current_time<="12:00:00":
    t("Good morning")
else:
    t("Good evening")
t('hi i am your assistant')
t("how can i help you")
#loop to continue executing multiple commands
while k:
    assistant(myCommand())
