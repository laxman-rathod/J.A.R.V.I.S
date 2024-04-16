from jarvis_speech_recognizer import listen, speak
import pyautogui
import ctypes
import datetime
import time
import os
# import configparser
    
def sleep_jarvis(query):
    speak("Okay sir, You can call me anytime")
    query = query.replace("jarvis", "").replace("you can", "").replace("wait", "").replace("sleep", "").replace("for", "").replace("seconds", "").replace("second", "").replace(" ", "")
    # print(f"Sir, I will wait for {query} seconds.....")
    time.sleep(int(query))
    speak("Hello sir! I am here, what should I do?")
    
def exit_jarvis():
    speak("Are you sure, sir?")
    res = listen()
    if "yes" in res or "confirm" in res or "yes i'm sure" in res or "yes i am sure" in res:
        speak("Okay sir! Goodbye.")
        exit()
    else:
        speak("Alright sir! I am here.")

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    msg = "Sir, what's the new plan for today?"
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning sir! {msg}")
    elif hour > 12 and hour <= 18:
        speak(f"Good Afternoon sir! {msg}")
    else:
        speak(f"Good Evening sir! {msg}")

def remember_that(query):
    rememberMessage = query.replace("remember that","").replace("jarvis","")
    speak("Sure sir! I will remembered that "+rememberMessage)
    remember = open("Remember.txt","w")
    remember.write(rememberMessage)
    remember.close()
    
def say_what_rem():
    remember = open("Remember.txt","r")
    speak("Sir you told me to remember that" + remember.read())

def shutdown_system():
    speak("Sir, are you sure? To shutting down the system?")
    res = listen()
    if res == "yes" or res == "confirm" "yes i am sure" == res:
        speak("System is shutting down..")
        os.system("shutdown /s /t 1")
    else:
        speak("System will not shut down, sir.")
        
def system_lock(): 
    speak("Okay sir, now i am locking the system.")   
    try:
        ctypes.windll.user32.LockWorkStation()
        speak("System locked successfully.")
    except Exception:
        speak("Sir something went wrong.")
        
def login_windows():
    # config = configparser.ConfigParser()# Create a configparser object
    # config.read('secrets.ini')# Load the INI file
    # speak("Sir, after a few seconds, the system will be logged in.")
    
    # password = config.get('secrets', 'password')# Get the secrets
    # # time.sleep(2) # Delay for a few seconds to switch to the login screen
    # pyautogui.press('enter')
    # pyautogui.typewrite(password)# Type the password
    # pyautogui.press('enter')
    # speak("Sir, the system has been successfully logged in.")
    pass