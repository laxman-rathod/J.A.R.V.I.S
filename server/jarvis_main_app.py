# from jarvis_speech_recognizer import listen, speak
# from whatsapp_automation import sendMessage
# from dict_apps import *
# from date_time import *
# from weather_temperature import *
# from password_auth_jarvis import *
# from quick_actions import *
# from automate_task import *
# import conversation
# from play_music import *
# import search_now
# import type_automatically


# from flask import Flask, jsonify
# from flask_cors import CORS
# import llama2_nlp

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# @app.route('/', methods=['GET'])
# def home_page():
#     msg = {"msg": "Welcome to Homepage!"}
#     return jsonify(msg)

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     print("Jarvis is online.")
#     while True: 
#         command = listen()
        
#         if command:
#             print(f"You: {command}")
#             return handle_command(command)
                
# def handle_command(command):
#     if "wake up" in command or "greet me" in command:
#         greetMe()
        
#     elif "time" in command:
#         get_current_time()
        
#     elif "open" in command:
#         openappweb(command)
        
#     elif "close" in command:
#         closeappweb(command)
        
#     elif "type" in command:
#         type_automatically.type_something(command)
        
#     elif "message" in command:
#         sendMessage()
        
#     elif "what is today" in command:
#         get_date_and_location() 
        
#     elif "your name" in command or "who are you" in command:
#         conversation.intro_about_jarvis()
        
#     elif "search" in command:
#         search_now.search_about(command)
        
#     elif "temperature" in command:
#         current_temperature(command)

#     elif "weather" in command:
#         todays_weather(command)

#     elif "internet speed" in command:
#         show_internet_speed()
        
#     elif "remember" in command:
#         remember_that(command)

#     elif "what do you remember" in command or "what i said" in command:
#         say_what_rem()
#         # remember = open("Remember.txt","r")
#         # speak("Sir you told me to remember that" + remember.read())

#     elif "alarm" in command:
#         set_alarm()

#     elif "snooze" in command:
#         snooze_alarm()
#         speak("Alarm snoozed.")

#     elif "my photo" in command:
#         capture_photo()

#     elif "play music" in command:
#         speak("Playing your favorite song sir.")
#         play_song("./songs/Hawayein_song.mp3")

#     elif "stop music" in command:
#         stop_song()
#         speak("Music stopped.")

#     elif "change password" in command:
#         change_password()
        
#     elif "sleep" in command or "wait" in command:
#         sleep_jarvis(command)
        
#     elif "login" in command:
#         login_windows()
        
#     elif "lock" in command:
#         system_lock()
        
#     elif "exit" in command:
#         exit_jarvis()
        
#     elif "shutdown" in command:
#         shutdown_system()
        
#     # check gmails function goes here
                    
#     else:
#         # prompt = command.replace("jarvis", "")
#         # data = llama2_nlp.ask_to_llama2(prompt) # replace("gemini", "jarvis").replace("llama", "jarvis")
#         data = "I am doing well, thanks for asking."
#         speak(data)
#         return data
    
# if __name__ == '__main__':
#     app.run(debug=True)
