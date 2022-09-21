from inspect import indentsize
from pickle import FALSE
from turtle import pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

path_chd = "/Users/danniemarom/Dropbox/JDMR/UAQ/Ingeniera de Software/7MO SEM/PYA Calidad del Software/Selenium/chromedriver"
driver = webdriver.Chrome(path_chd)
driver.maximize_window()
print("Listo")

# get page
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(2)


# get source element 
source_element1 = driver.find_element(By.ID,"box1")
# get target element 
target_element1 = driver.find_element(By.ID,"box101")

# get source element 
source_element2 = driver.find_element(By.ID,"box2")
# get target element 
target_element2 = driver.find_element(By.ID,"box102")

# get source element 
source_element3 = driver.find_element(By.ID,"box3")
# get target element 
target_element3 = driver.find_element(By.ID,"box103")

# get source element 
source_element4 = driver.find_element(By.ID,"box4")
# get target element 
target_element4 = driver.find_element(By.ID,"box104")

# get source element 
source_element5 = driver.find_element(By.ID,"box5")
# get target element 
target_element5 = driver.find_element(By.ID,"box105")

# get source element 
source_element6 = driver.find_element(By.ID,"box6")
# get target element 
target_element6 = driver.find_element(By.ID,"box106")

# get source element 
source_element7 = driver.find_element(By.ID,"box7")
# get target element 
target_element7 = driver.find_element(By.ID,"box107")

# create action chain object
action = ActionChains(driver)

# drag and drop the item
action.drag_and_drop(source_element1, target_element1)
action.drag_and_drop(source_element2, target_element2)
action.drag_and_drop(source_element3, target_element3)
action.drag_and_drop(source_element4, target_element4)
action.drag_and_drop(source_element5, target_element5)
action.drag_and_drop(source_element6, target_element6)
action.drag_and_drop(source_element7, target_element7)

# perform the operation
action.perform()
print("Listo2")


driver.quit