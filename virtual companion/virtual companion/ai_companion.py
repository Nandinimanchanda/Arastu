import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
import pyttsx3
import threading
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests
import tkinter as tk
from PIL import Image

#
text_content = ""
#text_content2 ="...............things you can make me do .................\n\n 1.say Open google\n\n 2.say Open Youtube\n\n 3. say Play Music\n\n4. say open weather forecast \n\n 5. TAlk to me like a friend \n\n 6. say open code to open visual studio code \n\n 7.say Tell me a story\n\n 8. Search wikipedia\n\n9. and alot else you can make  me do for you..........."
def start():
    count=0
    threading.Thread(target=MainExecution).start()


def create_wrapped_label(master, text, wraplength):
    label = tk.Label(master, text=text, wraplength=wraplength,height=100,width=200)
    label.pack()
    return label

def create_frame(master, side, color):
    frame = tk.Frame(master, width=20, height=10, bg=color)
    frame.pack(side=side, fill="both", expand=True)
    return frame

root = tk.Tk()
root.title("Ai_Companion")

def MainExecution():
    global text_content
    print("")
    print("NAMASTE welcome to ARASTU")
    text_content=text_content + "\n\nNAMASTE welcome to ARASTU. " # type: ignore
    text_label.configure(text="\n\nNAMASTE welcome to ARASTU. ")
    print("")
    Speak("Hello, welcome to ARASTU, I am your virtual Friend.")


    while True:

        Data = MicExecution()
        Data = str(Data)
        Data = Data.lower()
        getResponse(Data)


def getResponse(Data):
        DataLen = len(Data)

        if "introduce yourself" in Data:
           Speak("Hello! I am your dedicated digital assistant, poised to simplify your daily tasks, streamline your workflow, and enhance overall efficiency. Whether you need information, assistance, or just a friendly chat, I'm here to make your digital experience seamless and enjoyable.")
        elif int(DataLen)<=1:
            pass
        if 'wikipedia' in Data:
            Speak('Searching Wikipedia...')
            Data = Data.replace("wikipedia", "")
            results = wikipedia.summary(Data, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)

        elif 'open youtube' in Data:
            webbrowser.open("youtube.com")
        elif 'open weather forecast' in Data:
            webbrowser.open("accuweather.com")

        elif 'open google' in Data:
            webbrowser.open("google.com")
        elif 'play music' in Data:
            music_dir = 'C:\\Users\\HP\\Music\\favourite'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}")

        elif 'open code' in Data:
            codePath = "C:\\Users\\nandi\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
        
        elif 'open file' in Data:
            codePath = "C:\\Users\\HP\\Desktop\\File Explorer.lnk"
            os.startfile(codePath)

        elif 'hello' in Data:
            Speak(" hello master,  , i am there to help you out ")

        elif 'i am fine' in Data:
            Speak("happy to hear this nandini , hope you will recover from your anxiety soon")

        elif 'oh you care for me' in Data:
            Speak(" yes my lord, am there for you ")

        elif 'bye' in Data:
            Speak("bye sir hope to meet you soon ")

        elif 'thank you' in Data:
            Speak("most welcome sir")
        elif 'favourtie singer' in Data:
            Speak("my favourite singer is ASha bhosale")
        elif'tell me a story' in Data:
            Speak("Once there was a Lion in the jungle who used to kill 2-3 animals daily for his meal. All animals went to him to tell, that daily one of them will come to him for his meal.So, the Lion agreed and this started going for many days. One day, it was Rabbit’s turn. When he was on his way he saw a well.Now he plans to kill the lion and save himself. He went to the lion and told him that, there is another lion who claims to be more powerful than him.Then the lion asks the rabbit to take him to that lion. The rabbit takes him to the well and said he lives here. When the lion looked in the well he saw his own reflection and jumped in the well and dies.Moral: Wisdom wins might.")

        elif 'I am feeling alone and depressed' in Data:
            Speak("boss am there to help you out please do not feel lonely,share with me and light up your vibes")   

        else:
          r= requests.get("http://api.brainshop.ai/get?bid=171149&key=vUQ8EIQHjwgyJHYI&uid=[uid]&msg="+ Data)
          response_json = r.json()
          d = response_json["cnt"]  
          print(d)
          Speak(d)


#Functions
#Speak  
def Speak(Text):
    global text_content
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"You : {Text}.")
    print("")
    text_content=text_content+"\n\nArastu: "+Text # type: ignore
    text_label.configure(text=Text)
    engine.say(Text)
    engine.runAndWait()

# 1. listen 
def Listen():
    global text_content
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        text_content=text_content+"\n\nListening..." # type: ignore
        text_label.configure(text="\n\nListening...")
        r.energy_threshold=4000
        r.pause_threshold = 1
        audio = r.listen(source,20,None) # Listening Mode.....

    try:
        print("Recognizing...")
        text_content=text_content+"\n\nRecognizing..."
        text_label.configure(text="\n\nRecognizing...")
        query = r.recognize_google(audio,language="en") # type: ignore
        

    except:
        return ""

    query = str(query).lower()
    text_content=text_content+"\n\nYou:"+query # type: ignore
    return query

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text #  type: ignore
    print(f"You : {data}.")
    # text_content=text_content+"\n\n YOU:"
    # scrollable_label.configure(text=text_content)
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data


file = "D:\\python 3.8\\projects\\static\\NTHO.gif"
info = Image.open(file)
frames = info.n_frames
print(frames)

im = [tk.PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
gif_label = tk.Label(root, image="")
gif_label.configure(background='black')
gif_label.pack()

b1 = tk.Button(root, text="Wake Up Me", fg="white", background="black", font=("Helvetica", 15),
              command=start)
b1.pack(pady=10)

text_label = tk.Label(root,text="",font=("Helvetica", 15),wraplength=400)
text_label.pack()


def animation(count):
    im2 = im[count]
    gif_label.configure(image=im2)

    count += 1
    if count == frames:
        count = 0

    root.after(50, lambda: animation(count))
threading.Thread(target=animation(0)).start()

root.mainloop()