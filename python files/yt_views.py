from selenium import webdriver 
import time
refresh_time_in_seconds = 46

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=Is1_jYDrIBw")
url = driver.current_url
while(True):
    if url == driver.current_url:
        driver.refresh()
    url = driver.current_url
    time.sleep(refresh_time_in_seconds)