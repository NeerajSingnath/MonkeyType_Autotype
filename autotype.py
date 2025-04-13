import time

from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

keyboard = Controller()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://monkeytype.com/")

current_time = 0

try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "acceptAll"))).click()
except Exception as e:
    print("Error: 'Accept All' button not found or clickable.", e)

time.sleep(5)
start_time = time.time()
try:
    while True:
        active_word = driver.find_element(
            By.CSS_SELECTOR, "#words .word.active")

        for char in active_word.text:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.05)

        end_time = time.time()

        keyboard.press(Key.space)
        keyboard.release(Key.space)
        if end_time - start_time > 30:
            break
except Exception as e:
    print("Error during typing:", e)

time.sleep(10)
driver.quit()
