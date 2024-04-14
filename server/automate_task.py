from jarvis_speech_recognizer import speak, listen
from play_music import stop_song, play_song
import pyautogui
import speedtest 

from datetime import datetime
import time

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
            speak("Sir Alarm activated!")
            time.sleep(1)
            speak("Sir.. Alarm activated!")
            break
        time.sleep(10) # Check every 10 seconds

def main_alarm(input_time):
    # speak("Please say the time followed by the time in format HH MM AM/PM.")
    # input_time = listen().replace(".", "")
    input_time = input_time.replace(".", "").replace("jarvis", "").replace("set", "").replace("set alarm", "").replace("alarm", "").replace("for", "").replace("at", "")
    if input_time:
        set_alarm_time(input_time)
        check_alarm()

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