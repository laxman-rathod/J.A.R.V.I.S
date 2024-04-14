import os 
import pyautogui
import webbrowser
from jarvis_speech_recognizer import speak

dictapp = {
    "commandprompt": "cmd",
    "paint": "mspaint",
    "word": "word",
    "excel": "excel",
    "brave": "brave",
    "edge": "msedge",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "calculator": "calculator",
    "settings": "settings",
    "gallery": "photos",
    "camera": "camera",
    "whatsapp": "whatsapp",
    "files": "file explorer",
}

def openappweb(query, msg="It's on your screen sir."):
    query = query.replace("open", "").replace("hey", "").replace("jarvis", "").strip()
    opening_msg = f"Opening {query}"
    if ".com" in query or ".co.in" in query or ".org.in" in query or ".in" in query or ".io" in query:
        speak(opening_msg)
        webbrowser.open(f"https://www.{query}")
        speak(msg) 
    else:
        for app, exe in dictapp.items():
            if app in query:
                speak(opening_msg)
                os.system(f"start {exe}")
                speak(msg)  
                break


def closeappweb(query, message="Sir tab closed."):
    if "tab" in query:
        pyautogui.hotkey('ctrl', 'w')
        speak(message)
    else:
        for app, exe in dictapp.items():
            if app in query:
                os.system(f"taskkill /f /im {exe}.exe")
                speak("Sir app closed.")
                break