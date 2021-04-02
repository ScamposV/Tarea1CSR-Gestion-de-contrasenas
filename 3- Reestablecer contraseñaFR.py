import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

options= webdriver.ChromeOptions()
driver_path="C:\\Users\\Tatán\\Desktop\\Tarea1-C&SR\\chromedriver.exe"

driver=webdriver.Chrome(driver_path, options=options)
driver.set_window_size(1360,1080)
driver.get("https://www.probikeshop.fr/")

Cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
Cookies.click()
MiCuenta =driver.find_element_by_css_selector("#link_myAccount > img")
MiCuenta.click()
driver.find_element_by_class_name("shoppingcart_zoneLink").click()
email = driver.find_element_by_id("email")
email.click()
email.send_keys("tareaparael8@gmail.com")
driver.find_element_by_class_name("newPasswordForm_submit").click()
