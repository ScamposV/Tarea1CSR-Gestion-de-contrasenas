import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

options= webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
driver_path="C:\\Users\\Tatán\\Desktop\\Tarea1-C&SR\\chromedriver.exe"

driver=webdriver.Chrome(driver_path, options=options)
driver.set_window_size(1360,1080)
driver.get("https://www.fantasilandia.cl/")

MiCuenta = driver.find_element_by_class_name("btn-group").click()
time.sleep(2)
Imail = driver.find_element_by_name("txtUser")
Imail.send_keys("tareaparael8@gmail.com")
Ipass = driver.find_element_by_name("txtPassword")
Ipass.send_keys("Tareaparael8")
driver.find_element_by_id("btnEnviarTop").click()

