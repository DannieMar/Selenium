from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path_chd = "/Users/danniemarom/Dropbox/JDMR/UAQ/Ingeniera de Software/7MO SEM/PYA Calidad del Software/Selenium/chromedriver"
driver = webdriver.Chrome(path_chd)
driver.get("https://github.com/login")

#time.sleep(5) #detiene el proceso del script

user = driver.find_element(By.ID,"login_field")
password = driver.find_element(By.ID,"password")
user.send_keys("DannieMar")
password.send_keys("Marley3017")
user.send_keys(Keys.ENTER)