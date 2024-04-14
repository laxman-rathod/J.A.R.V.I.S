from datetime import datetime
import geocoder
from jarvis_speech_recognizer import speak

# Function to get the current time
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  # 12-hour format
    time_msg = f"The current time is {current_time}"
    print(time_msg)
    speak(time_msg)

# Get the current date and locantion of user.
def get_date_and_location():
    now = datetime.now()
    formatted_date = now.strftime("%A, %d %B %Y")
    g = geocoder.ip('me') # Get the current location
    location = g.city + ", " + g.state
    date_msg = "Sir Today is " + formatted_date
    location_msg = "Date in " + location
    print(date_msg)
    speak(date_msg)
    print(location_msg)
    speak(location_msg)