#Checkbox dynamically using selenium

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

option = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
time.sleep(3)
print(len(option))

'''using for loop to find the element you want, when you dont know were the value is located'''
for checkbox in option:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        #is_selected() - to check whether the checkbox is selected or not - returns boolean value
        assert checkbox.is_selected()
        break
time.sleep(5)
