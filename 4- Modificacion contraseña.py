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
Imail = driver.find_element_by_name("txtUser")
Imail.click()
Imail.send_keys("tareaparael8@gmail.com")
Ipass = driver.find_element_by_name("txtPassword")
Ipass.click()
Ipass.send_keys("Tareaparael7")
iniciosesion = driver.find_element_by_id("btnEnviarTop")
iniciosesion.click()

#########################################################################
#                       MODIFICACION DE CONTRASEÑA                      #
#########################################################################
time.sleep(20)
Cpass = driver.find_element_by_css_selector ("#main > div > div.row > div.col-md-3 > div > ul > li:nth-child(6) > a")
Cpass.click()
time.sleep(3)
Apass = driver.find_element_by_css_selector ("#passActual")
Apass.click()
Apass.send_keys("Tareaparael7")
Npass = driver.find_element_by_css_selector ("#passNueva")
Npass.click()
#UTF-8
Npass.send_keys("123456789a123456789b123456789c123456789d123456789e123456789f123456789g12123456789a123456789b123456789c123456789d123456789e123456789f123456789g12123456789a123456789b123456789c123456789d123456789e123456789f123456789g12")
RNpass = driver.find_element_by_css_selector ("#passNuevaRe")
RNpass.click()
RNpass.send_keys("123456789a123456789b123456789c123456789d123456789e123456789f123456789g12123456789a123456789b123456789c123456789d123456789e123456789f123456789g12123456789a123456789b123456789c123456789d123456789e123456789f123456789g12")
save = driver.find_element_by_css_selector ("#btnCambiarPass")
save.click()
