import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine and recognizer
engine = pyttsx3.init("sapi5")
recognizer = sr.Recognizer()

# Convert text to speech with improved clarity and rate settings
def speak(text):
    engine.say(text)
    engine.setProperty('rate', 180)  # Adjust rate for natural-sounding speech (150-220 range)
    engine.runAndWait()

# Listen to user input, handling timeout and errors gracefully
def listen():
    with sr.Microphone() as source:
        print("I am Listening... \n")
        # recognizer.pause_threshold = 1  # Pause threshold for speech detection
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise

        try:
            audio = recognizer.listen(source, timeout=60)  # Timeout after 30 seconds
            text = recognizer.recognize_google(audio)
            return text.lower()  # Convert to lowercase for case-insensitive handling
        except sr.UnknownValueError:
            print("Sir I didn't understand that.")
            speak("Sir I didn't understand that.")
            return None
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))
            speak("There seems to be a connection error. Please check your internet connection and try again.")
            return None
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            speak("I didn't hear anything. Please speak again.")
            return None
        
        
# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# # Initialize speech recognition
# recognizer = sr.Recognizer()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     try:
#         command = recognizer.recognize_google(audio)
#         print("You said:", command)
#         return command
#     except sr.UnknownValueError:
#         print("Could not understand the audio.")
#         return ""
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#         return ""