import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyautogui
import os
import pywhatkit

en= pyttsx3.init('sapi5')
voices= en.getProperty("voices")
en.setProperty('voice', voices[1].id)
print(voices)

r = sr.Recognizer()

#def cmd(command):
   #os.system(command)

def quit(close):
   pyautogui.hostkey(close)

def speak(audio):
   en.say(audio)
   en.runAndWait()

def web(browser):
   webbrowser.open(browser)

def ss():
   im1 = pyautogui.screenshot()
   im1.save("screenshot.png")
   

def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12 :
      speak("Good MOrning..")
   elif hour>12 and hour<18:
      speak("Good Afternoon..")
   else:
      speak("Good Evening..")
   speak("Sir....") 

def takeCmd():
   
   
   with sr.Microphone() as source:
      print("Listening.......")
      r.pause_threshold = 1
      audio=r.listen(source)

      try:
         print("Recognizing....")
         query = r.recognize_google(audio, language='en-in')
         print("User said ",query)
         return query

      except Exception as e:
         #print(e) 
         speak("I cant recognize sir .....")

         
         return "None"  

# def cmd():
   
   #with sr.Microphone() as s:
      #print("Listening.......")
      #r.pause_threshold = 1
      #audio=r.listen(s)

      #try:
         #print("Recognizing....")
         #q = r.recognize_google(audio, language='en-in')
         #print("User said ",q)
        # return q

     # except Exception as e:
         #print(e) 
         #speak("Say again..")

         #speak("Say thet again daddy please.....")
        # return "None"     



if __name__=="__main__":
   wishme()
   speak("how may i help you Sir....")

   while True:
      

      query=takeCmd().lower()
      #q=cmd().lower()


      if "what is your name" == query or "your name "==query:
         speak("My name is esabellaa your personal A.I assistent...")
      elif "hey" == query :
         speak("Yess Sir how can i help you..")
      elif "bye" == query or "tata" == query :
         speak("Good bye .....")
         break
      elif "open youtube" == query:
         speak("opening  youtube ....")
         web("https://www.youtube.com/")

      elif "Close ".lower() == query.lower() or "youtube".lower()==query.lower():
         speak("Closing youtube sir ....")
         quit("ctrl","w")
      
      elif " take a screenshot" == query or"Screenshot"==query:
         speak("taking screenshot...")
         ss()

      #elif "play a song"==query:
        # speak("which song..")
        # if q==query:
           #  pywhatkit.playonyt(q)
        # else :
            #speak("Say again..")
      elif "open notepad"==query:
         speak("opening notepad")
         os.system("notepad")
      elif "how are you"==query:
         speak("I am fine what about you....")
      elif "your creater"==query or "your creator"==query:
         speak("My sir Soumyadip..")
      elif "open anime website"==query:
         speak("Oening Aniwatch..")
         webbrowser.open_new_tab("https://aniwatchtv.to/home")
      elif "play my favourite song"==query:
         pywhatkit.playonyt("Jee karda")
      elif "are you here"==query or "you here"==query:
         speak("Yesss Sirrr , I am here ...")
         
      elif "Open Calculator" ==query.lower():
         speak("Opening Calculator")
         os.system("calc")
      


   



      
      


