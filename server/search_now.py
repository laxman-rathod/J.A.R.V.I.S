import pywhatkit
import wikipedia
import webbrowser
from jarvis_speech_recognizer import speak

def search_about(query):
    query = query.replace("jarvis", "").replace("search on", "").replace("play", "").replace("about", "")
    msg = f"Sir this is what I found on {query}"
    
    if "google" in query:
        speak(msg)
        query = query.replace("google", "")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except Exception as e:
            speak("Sir, no speakable output available")

    elif "youtube" in query:
        speak(msg)
        query = query.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done Sir")

    elif "wikipedia" in query:
        speak("Searching on Wikipedia Sir....")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("Sir, According to wikipedia.")
            speak(results)
        except:
            speak("Sorry sir, Page is not available.")
            
    else:
        speak("Sir, please provide valid input.")