import datetime
import pywhatkit
from datetime import timedelta
from datetime import datetime
from jarvis_speech_recognizer import speak, listen

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 1)).strftime("%M"))

def sendMessage():
    speak("Whats the message sir?")
    message = listen()
    if message:
        speak(f"Sending {message} message sir")
        pywhatkit.sendwhatmsg("+919764701233", message, time_hour = strTime, time_min = update)
        # print("Sir Message sent successfully!")
        speak("Sir Message sent successfully!")