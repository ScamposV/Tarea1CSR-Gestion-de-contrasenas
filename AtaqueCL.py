import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random
import time

contras = ["0","Tareaparael7","Tareaparael8", "123456789a123456789b123456789c123456789d123456789e123456789f123456789g12", "❤", "!&%/&/)&/%&", "asdasda", "qiwudh78sayd32892hnb4 23 4u23423"]

for i in range(0,100):
    print("Intento: ",i+1)
    options= webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    driver_path="C:\\Users\\Tatán\\Desktop\\Tarea1-C&SR\\chromedriver.exe"

    driver=webdriver.Chrome(driver_path, options=options)
    driver.set_window_size(1360,1080)
    driver.get("https://www.fantasilandia.cl/")

    MiCuenta = driver.find_element_by_class_name("btn-group")
    MiCuenta.click()
    time.sleep(2)
    Imail = driver.find_element_by_name("txtUser")
    Imail.click()
    Imail.send_keys("tareaparael8@gmail.com")
    Ipass = driver.find_element_by_name("txtPassword")
    Ipass.click()
    
    p=random.choice(contras)
    Ipass.send_keys(p)
    
    iniciosesion = driver.find_element_by_id("btnEnviarTop")
    iniciosesion.click()
    time.sleep(10)
    driver.quit()
