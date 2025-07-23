from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as rq
import time 

def finding_place_to_eat(food_name):
    dining="https://www.naver.com/"
    options = wb.ChromeOptions()
    prefs={"profile.default_content_setting_values.geolocation":1} 
    options.add_experimental_option("prefs", prefs)
    options.add_argument('headless') 
    options.add_argument('window-size=1920x1080') 
    options.add_argument("no-sandbox") 
    options.add_argument("disable-dev-shm-usage") 
    driver = wb.Chrome(options=options)
    driver.get(dining)
    time.sleep(2)
    driver.maximize_window()
    
    search_dining = driver.find_element(By.CSS_SELECTOR, ".search_input")
    search_dining.click()
    search_dining.send_keys(f"{food_name} 맛집")
    search_dining.send_keys(Keys.ENTER)
    cur_url = driver.find_element(By.CSS_SELECTOR, ".bSoi3>a").get_attribute("href")
    return cur_url