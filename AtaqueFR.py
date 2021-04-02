import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

contras = ["0", "123456789a123456789b123456789c123456789d123456789e123456789f123456789g12", "❤", "!&%/&/)&/%&", "asdasda", "qiwudh78sayd32892hnb4 23 4u23423"]

for i in range(0,100):
    print("Intento: ",i+1)
    options= webdriver.ChromeOptions()
    driver_path="C:\\Users\\Tatán\\Desktop\\Tarea1-C&SR\\chromedriver.exe"

    driver=webdriver.Chrome(driver_path, options=options)
    driver.set_window_size(1360,1080)
    driver.get("https://www.probikeshop.fr/")
    
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    driver.find_element_by_css_selector("#link_myAccount > img").click()
    email = driver.find_element_by_id("email")
    email.send_keys("tareaparael8@gmail.com")
    passw = driver.find_element_by_css_selector("#password")
    
    p=random.choice(contras)
    passw.send_keys(p)
    
    driver.find_element_by_class_name("login_button").click()
    time.sleep(3)
    driver.quit()
