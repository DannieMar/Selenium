from inspect import indentsize
from pickle import FALSE
from turtle import pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

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
time.sleep(1)

txt_columns = driver.find_element(By.XPATH, "//*[@id=\"cityTable\"]/div[1]/ul")
txt_columns = txt_columns.text

todays_wheater = txt_columns.split('Hoy')[0].split('\n')[1:1]

horas= list()
temp= list()
v_viento = list()

for i in range(0, len(todays_wheater),3):
        horas.append(todays_wheater[i])
        temp.append(todays_wheater[i+1])
        v_viento.append(todays_wheater[i+2])
df = pd.DataFrame({'Horas':horas},{'Temperatura':temp},{'v_viento(km/h):v_viento'})
print (df)
print ("Listo")

#to send excel
df.to_csv('tiempo_hoy.csv',index=False)

driver.quit