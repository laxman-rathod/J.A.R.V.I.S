

# elif "snooze" in command:
#         snooze_alarm()
#         speak("Alarm snoozed.")

from datetime import datetime
import pyttsx3
import speech_recognition as sr
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def set_alarm_time(input_time):
    try:
        input_formatted_time = datetime.strptime(input_time, '%I:%M %p')
        formatted_time = input_formatted_time.strftime('%I:%M %p')
        with open("Alarmtext.txt", "w") as time_file:
            time_file.write(formatted_time)
        print(f"Alarm set for {formatted_time}.")
        speak(f"Alarm set for {formatted_time}.")
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM AM/PM format.")
        return

def check_alarm():
    with open("Alarmtext.txt", "r") as file:
        alarm_time = file.read().strip()
    while True:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        if current_time == alarm_time:
            speak("Alarm activated! It's time.")
            break
        time.sleep(10) # Check every 10 seconds

if __name__ == "__main__":
    # speak("Please say the time followed by the time in format HH MM AM/PM.")
    # input_time = "3:15 p.m."
    input_time = listen().replace(".", "")
    print(input_time)
    
    if input_time:
        set_alarm_time(input_time)
        check_alarm()