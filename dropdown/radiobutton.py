#Radio button automation method

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radiobutton = driver.find_elements(By.CSS_SELECTOR,".radioButton")
print(len(radiobutton))
radiobutton[2].click( )
time.sleep(3)

#to check whether the radio button is selected or not - returns boolean value
assert radiobutton[2].is_selected()

#to check whether the element is displayed or not - returns boolean value
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(2)

