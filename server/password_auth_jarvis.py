from jarvis_speech_recognizer import speak

def jarvis_auth():
    for i in range(3):
        a = input("Enter Password to open Jarvis :- ")
        pw_file = open("password.txt","r")
        pw = pw_file.read()
        pw_file.close()
        if (a==pw):
            print("Welcome sir! Please speak 'Jarvis wake up' to load up me.")
            speak("Welcome sir! Please speak 'Jarvis wake up' to load up me.")
            break
        elif (i==2 and a!=pw):
            exit()
        elif (a!=pw):
            print("Try Again")

def change_password():
    speak("What's the new password sir?")
    new_pw = input("Enter the new password\n")
    new_password = open("password.txt","w")
    new_password.write(new_pw)
    new_password.close()
    speak("Done sir")
    speak(f"Your new password is{new_pw}")