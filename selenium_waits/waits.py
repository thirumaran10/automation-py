#chaining of web elements spliting the xpath of parent and child elements and chaining them
#implicit wait and explicit waits in selenium

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 

driver = webdriver.Chrome()
driver.implicitly_wait(5) #implicit wait - applies to all the elements
driver.get("https://rahulshettyacademy.com/seleniumPractise/?utm_source=chatgpt.com#/")
driver.maximize_window()

driver.find_element(By.XPATH,'//input[@type="search"]').send_keys("ber")
time.sleep(2)

#plural form - to get multiple elements 
results = driver.find_elements(By.XPATH,'//div[@class="product"]')
count = len(results)
assert count > 0

for result in results:
#chaining of webelements, (result already having the xpath of parent element from that we adding the child element xpath)
    result.find_element(By.XPATH,'.//div/button').click()

driver.find_element(By.XPATH,'//img[@alt="Cart"]').click()
driver.find_element(By.XPATH,"//button[text() = 'PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

#explicit wait - applies to specific element
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[text()='Code applied ..!']")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

driver.find_element(By.XPATH,"//button[text() = 'Place Order']").click()

driver.find_element(By.XPATH,'//option[@value="India"]').click()
driver.find_element(By.CLASS_NAME,"chkAgree").click()

driver.find_element(By.XPATH,"//button[text() = 'Proceed']").click()

time.sleep(5)