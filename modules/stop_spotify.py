from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from jarvis_speech_recognizer import speak

def stop_spotify():
    speak("Sure sir.")
    
    chrome_driver_path = r"C:/WebDrivers/chrome-win64/chromedriver.exe"
    
    driver = webdriver.Chrome(executable_path = chrome_driver_path) # executable_path=chrome_driver_path

    # Navigate to the Spotify web player
    driver.get("https://open.spotify.com")

    # Wait for the page to load
    time.sleep(2)

    # Find the player control buttons
    player_controls = driver.find_element_by_class_name("encore-bright-accent-set")

    # Find the pause button and click it
    pause_button = player_controls.find_element_by_xpath(".//button[@data-testid='control-button-toggle-play']")
    pause_button.click()

    # Wait for the music to stop playing
    time.sleep(2)
    speak("Music stopped.")

    # Close the browser
    # driver.quit()