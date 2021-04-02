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
#maximo 96 caracteres
email = driver.find_element_by_id("email")
email.click()
email.send_keys("tareaparael8@gmail.com")
passw = driver.find_element_by_css_selector("#password")
passw.click()
passw.send_keys("123456789a123456789b123456789c123456789d123456789e123456789f123456789g12")
driver.find_element_by_class_name("login_button").click()

#########################################################################
#                       MODIFICACION DE CONTRASEÑA                      #
#########################################################################
time.sleep(3)
a = driver.find_element_by_link_text("Changer le mot de passe de mon compte")
a.click()
apass = driver.find_element_by_id("changepass_current_password")
apass.click()
apass.send_keys("123456789a123456789b123456789c123456789d123456789e123456789f123456789g12")
npass = driver.find_element_by_id("changepass_newpassword")
npass.click()
npass.send_keys("123456789a123456789b123456789c123456789d123456789e123456789f123456789g12")
rpass = driver.find_element_by_id("changepass_renewpassword")
rpass.click()
rpass.send_keys("123456789a123456789b123456789c123456789d123456789e123456789f123456789g12")
time.sleep(3)
driver.find_element_by_css_selector("body > div.off-canvas-wrapper > div > div > div.account_edit > div.customer_form > form > div.customerForm_submit > input[type=submit]").click()

