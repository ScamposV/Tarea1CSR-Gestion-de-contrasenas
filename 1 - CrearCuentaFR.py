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
Crear = driver.find_element_by_class_name("blue-button")
Crear.click()
driver.find_element_by_id("male").click()
Nombre = driver.find_element_by_name("firstname")
Nombre.click()
Nombre.send_keys("Sebastian")
ApeP = driver.find_element_by_name("lastname")
ApeP.click()
ApeP.send_keys("Campos")
Dia = driver.find_element_by_id("birthdate_day")
Dia.click()
Dia.send_keys("30")
Mes = driver.find_element_by_css_selector("#birthdate_month > option:nth-child(8)")
Mes.click()
Year = driver.find_element_by_id("birthdate_year")
Year.click()
Year.send_keys("1996")
email = driver.find_element_by_id("email")
email.click()
email.send_keys("tareaparael8@gmail.com")
Pass = driver.find_element_by_id("password")
Pass.click()
Pass.send_keys("Tareaparael8")
Adress = driver.find_element_by_id("address")
Adress.click()
Adress.send_keys("No se llama")
Postal = driver.find_element_by_id("zipcode")
Postal.click()
Postal.send_keys("5426132")
City = driver.find_element_by_id("city")
City.click()
City.send_keys("Amall es on")
aipon2 = driver.find_element_by_class_name("react-phone-number-input__input.react-phone-number-input__phone")
aipon2.send_keys("953214411")
time.sleep(2)
driver.find_element_by_name("submit").click()
