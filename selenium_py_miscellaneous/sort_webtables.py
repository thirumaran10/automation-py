#sort the web page tables using selenium python - logic build
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browsersortveggies = []#empty string to stor the names
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/?utm_source=chatgpt.com#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

#click on column header
driver.find_element(By.XPATH,'//*[text() = "Veg/fruit name"]').click()
#collect all veggie names -> Browser sorted veggie list (A,B,C)
veggiewebelements = driver.find_elements(By.XPATH,"//tr/td[1]")#plural form
for veg in veggiewebelements:
    browsersortveggies.append(veg.text)#append add the items at end of the list

'''before sorting we store the names in new object, 
because after sorting the list the sorted names stors in same object
when creating a new copy of the list use (.copy) method'''  
original_sortedlist = browsersortveggies.copy()

#sorting the browsersortveggies list => new sorted list
browsersortveggies.sort()

assert browsersortveggies == original_sortedlist
time.sleep(10)
