from bs4 import BeautifulSoup
from jarvis_speech_recognizer import speak
import requests

def current_temperature(query):
    query = query.replace("today's", "").replace("current", "").replace("what is", "").replace("what is the", "")
    url = f"https://www.google.com/search?q={query}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{query} is {temp}")

def todays_weather(query):
    query = query.replace("today's", "").replace("current", "").replace("what is the", "")
    url = f"https://www.google.com/search?q={query}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{query} is {temp}")