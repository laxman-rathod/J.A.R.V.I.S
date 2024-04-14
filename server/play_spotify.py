from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from jarvis_speech_recognizer import speak

def play_spotify():
    speak("Playing your favorite song sir.")
    chrome_driver_path = r"C:/WebDrivers/chrome-win64/chrome.exe"

    # Create a Service instance with the path to the ChromeDriver
    service = Service(chrome_driver_path)

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service)

    # Navigate to the Spotify web player
    driver.get("https://open.spotify.com")

    # Wait for the page to load
    time.sleep(2)

    # Find the search box and enter the song or artist you want to play
    search_box = driver.find_element_by_xpath("//input[@data-testid='search-input']")
    search_box.send_keys("pal")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)

    # Find and click the first search result
    first_result = driver.find_element_by_xpath("//div[@data-testid='tracklist-row']")
    first_result.click()

    # Wait for the song to start playing
    time.sleep(2)

    # Close the browser
    driver.quit()

play_spotify()