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

for checkbox in option:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        print("checkbox 2 is_selected")
time.sleep(2)
