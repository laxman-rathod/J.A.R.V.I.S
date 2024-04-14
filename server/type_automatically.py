import pyautogui
import time
from jarvis_speech_recognizer import speak

def type_something(prompt): 
    prompt = prompt.replace("jarvis", "").replace("type", "")
    time.sleep(2)
    pyautogui.typewrite(prompt)
    pyautogui.press("enter")
    time.sleep(2) # Wait for a few seconds to see the result
    speak("Done sir!")