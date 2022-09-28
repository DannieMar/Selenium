from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 
import time

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

path_chd = "/Users/danniemarom/Dropbox/JDMR/UAQ/Ingeniera de Software/7MO SEM/PYA Calidad del Software/Selenium/chromedriver"
driver = webdriver.Chrome(path_chd)
driver.maximize_window()
driver.get("https://www.demoblaze.com/index.html")
alert = Alert(driver)


#### Registro
def registro():
	driver.find_element(By.ID, "signin2").click()
	time.sleep(3)
	driver.find_element(By.ID, "sign-username").send_keys("daniel12356789")
	driver.find_element(By.ID, "sign-password").send_keys("12345689")
	time.sleep(2)
	driver.find_element(By.XPATH, "//button[contains(text(),\'Sign up\')]").click()
	time.sleep(3)
	alert.accept()  

########Login#####
def login():
	driver.find_element(By.ID, "login2").click()
	time.sleep(3)
	driver.find_element(By.ID, "loginusername").send_keys("daniel12356789")
	driver.find_element(By.ID, "loginpassword").send_keys("12345689")
	time.sleep(2)
	driver.find_element(By.XPATH, "//button[contains(text(),\'Log in\')]").click()
	time.sleep(2)

########Carrito de compras#####
def comprar(tipo, producto):
	driver.find_element(By.XPATH, "//a[contains(text(),\'" + tipo + "\')]").click()
	time.sleep(2)

	driver.find_element(By.XPATH, "//a[contains(text(),\'" + producto + "\')]").click()
	time.sleep(3)

	driver.find_element(By.XPATH, "//a[contains(text(),\'Add to cart\')]").click()
	time.sleep(2)
	alert.accept() 
	time.sleep(2)

	driver.find_element(By.XPATH, "//a[contains(text(),\'Home \')]").click()

def vercarrito():
	driver.find_element(By.XPATH, "//a[contains(text(),\'Cart\')]").click()


registro()
login()
comprar("Phones", "Iphone 6 32gb")
comprar("Laptops", "Sony vaio i7")
time.sleep(2)
vercarrito()