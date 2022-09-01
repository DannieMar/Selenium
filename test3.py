from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path_chd = "/Users/danniemarom/Dropbox/JDMR/UAQ/Ingeniera de Software/7MO SEM/PYA Calidad del Software/Selenium/chromedriver"
driver = webdriver.Chrome(path_chd)
driver.maximize_window()

driver.get("https://www.clima.com")

driver.find_element(By.XPATH, "//a[contains(@href, \'https://www.clima.com/mexico\')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id=\'term\']").send_keys("Queretaro")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id=\"search\"]/ul//span[contains(text(),'Querétaro, Estado de Querétaro de Arteaga')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(),\'Por horas\')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(),\'Días\')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(),\'Fin de semana\')]").click()
time.sleep(2)

print ("Done")