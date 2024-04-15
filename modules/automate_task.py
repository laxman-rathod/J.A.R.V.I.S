from jarvis_speech_recognizer import speak, listen
from play_music import stop_song, play_song
import pyautogui
import speedtest 

# import datetime
# import time

# def set_alarm_time(input_time):
#     try:
#         input_formatted_time = datetime.datetime.strptime(input_time, '%I:%M %p')
#         formatted_time = input_formatted_time.strftime('%I:%M %p')
        
#         return formatted_time
#     except ValueError:
#         speak("Sir please provide time like HH:MM AM/PM format.")
#         return None

# def check_alarm(alarm_time):
#     while True:
#         now = datetime.datetime.now()
#         current_time = now.strftime("%I:%M %p")
#         if current_time == alarm_time:
#             speak("Sir Alarm activated!")
#             speak("Sir.... Alarm activated!")
#             # Add your code to handle the alarm here
#             break
#         time.sleep(10)  # Check every 10 seconds

# def main_alarm(input_time):
#     input_time = input_time.replace("jarvis", "").replace("set", "").replace("alarm", "").replace(".", "").replace("for", "").replace("at", "").strip()
#     alarm_time = set_alarm_time(input_time)
#     if alarm_time:
#         speak(f"Alarm set for {alarm_time}")
#         check_alarm(alarm_time)

import datetime
import time
import threading
from jarvis_speech_recognizer import listen

def set_alarm_time(input_time):
    try:
        input_formatted_time = datetime.datetime.strptime(input_time, '%I:%M %p')
        formatted_time = input_formatted_time.strftime('%I:%M %p')
        return formatted_time
    except ValueError:
        speak("Sir please provide time like HH:MM AM/PM format.")
        return None

def check_alarm(alarm_time):
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        if current_time == alarm_time:
            speak("Sir Alarm activated!")
            speak("Sir........ Alarm activated!")
            # Add your code to handle the alarm here
            break
        time.sleep(10)  # Check every 10 seconds

def alarm_thread(alarm_time):
    check_alarm(alarm_time)

def main_alarm(input_time):
    input_time = input_time.replace("jarvis", "").replace("set", "").replace("alarm", "").replace(".", "").replace("for", "").replace("at", "").strip()
    alarm_time = set_alarm_time(input_time)
    alarm_thread = None  # Initialize alarm_thread to None
    if alarm_time:
        speak(f"Alarm set for {alarm_time}.")
        alarm_thread = threading.Thread(target=alarm_thread, args=(alarm_time,))
        alarm_thread.start()

def snooze_alarm():
    stop_song()

def capture_photo():
    speak("Opening camera.")
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    speak("Sir Smile Please")
    pyautogui.press("enter")
    speak("Sir, Photo clicked")  

def show_internet_speed():
    st = speedtest.Speedtest()
    speak("Checking interet speed, please wait.")
    try:
        download_bps = st.download()
        upload_bps = st.upload()
        download_mbps = download_bps / (1024 * 1024)
        upload_mbps = upload_bps / (1024 * 1024)
    except:
        speak("Unable to retrieve internet speed information.")
    speak(f"Download speed: {download_mbps:.2f} Mbps")
    speak(f"Upload speed: {upload_mbps:.2f} Mbps")

    if download_mbps >= 1:
        speak("Sir Internet speed looks good.")