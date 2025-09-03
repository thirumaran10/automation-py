#Get attribute of value to validate dynamic texts on browser

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
contries = driver.find_elements(By.XPATH,'//li[@class="ui-menu-item"]/child::a')
print(len(contries))

for country in contries:
    if country.text == "India":
        country.click()
        break
time.sleep(2)

#print(driver.find_element(By.ID,"autosuggest").text)
'''instude of using .text we use get_attribute("value") - its a java script method to get the value of attribute'''
#to get the value of text box
#print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
time.sleep(2)

