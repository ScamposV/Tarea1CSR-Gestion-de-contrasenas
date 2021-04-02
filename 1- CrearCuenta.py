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
Registrate = driver.find_element_by_link_text('Regístrate')
Registrate.click()
time.sleep(2)
RUT = driver.find_element_by_name("txtRut")
RUT.click()
RUT.send_keys("19403946-8")
Nombre = driver.find_element_by_name("txtNombres")
Nombre.click()
Nombre.send_keys("Sebastian Ignacio")
ApeP = driver.find_element_by_name("txtPaterno")
ApeP.click()
ApeP.send_keys("Campos")
ApeM = driver.find_element_by_name("txtMaterno")
ApeM.click()
ApeM.send_keys("Vega")
#Copy Selector donde salia <option value="masculino">Masculino</option>
SexoM = driver.find_element_by_css_selector("#comboSexo > option:nth-child(2)")
SexoM.click()
Fnac = driver.find_element_by_name("txtFNacimiento")
Fnac.click()
Fnac.clear()
Fnac.send_keys("30-06-1996")
email = driver.find_element_by_name("txtEmail")
email.click()
email.clear()
email.send_keys("tareaparael8@gmail.com")
Remail = driver.find_element_by_name("txtREmail")
Remail.click()
Remail.clear()
Remail.send_keys("tareaparael8@gmail.com")
Phone = driver.find_element_by_name("txtTelefonoFijo")
Phone.click()
Phone.clear()
CPhone = driver.find_element_by_name("txtTelefonoCelular")
CPhone.click()
CPhone.clear()
CPhone.send_keys("953215512")
#Copy Selector donde salia <option value="7">Metropolitana de Santiago</option>
RM = driver.find_element_by_css_selector("#comboRegion > option:nth-child(8)")
RM.click()
#tiempo necesario para que la opcion de la comuna pueda ser seleccionada
time.sleep(1)
#Copy Selector donde salia <option value="114">Maipú</option>
Maipudencia = driver.find_element_by_css_selector("#comboComuna > option:nth-child(34)")
Maipudencia.click()
Direccion = driver.find_element_by_name("txtDireccion")
Direccion.click()
Direccion.clear()
Direccion.send_keys("San Benito")
Stgo = driver.find_element_by_name("txtCiudad")
Stgo.click()
Stgo.clear()
Stgo.send_keys("Santiago")
Pass = driver.find_element_by_name("txtContrasena")
Pass.click()
Pass.clear()
Pass.send_keys("Tareaparael7")
RPass = driver.find_element_by_name("txtRepetirContrasena")
RPass.click()
RPass.clear()
RPass.send_keys("Tareaparael7")

Registrarse = driver.find_element_by_id("btnRegistrarse")
Registrarse.click()
