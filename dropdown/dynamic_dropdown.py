#auto suggestive dynamic dropdowns

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
#giving a variable to store the all matching elements 
#using find_elements to identify multiple elements (plural form)
contries = driver.find_elements(By.XPATH,'//li[@class="ui-menu-item"]/child::a')

#to identify the length of list, we using python len command
print(len(contries))

#.text extracts the visible text of that WebElement.
for country in contries:
    if country.text == "India":
        country.click()
        break

time.sleep(2)
