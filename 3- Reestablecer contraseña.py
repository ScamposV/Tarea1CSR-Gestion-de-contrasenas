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

MiCuenta = driver.find_element_by_class_name("btn-group")
MiCuenta.click()
time.sleep(2)
Opass = driver.find_element_by_class_name("aubnder")
Opass.click()
time.sleep(2)
Email = driver.find_element_by_name("email-recupera")
Email.click()
Email.send_keys("tareaparael8@gmail.com")
time.sleep(2)
Rpass = driver.find_element_by_css_selector("#exampleModalForm > div.modal-footer > button")
Rpass.click()
