#functional automation 
#sum validation and discount validation


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
time.sleep(5)

#plural form - to get multiple elements, to get the add to cart button
# get all product cards
products = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count = len(products)
assert count > 0
for p in products:
    # click the add-to-cart button inside this card
    p.find_element(By.XPATH, './div/button').click()

driver.find_element(By.XPATH,'//img[@alt="Cart"]').click()
driver.find_element(By.XPATH,"//button[text() = 'PROCEED TO CHECKOUT']").click()

#sum validation
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for amt in prices:
    sum = sum + int(amt.text) 
print(sum)
 
totalamt = int(driver.find_element(By.XPATH,'//div/span[@class="totAmt"]').text)
assert sum == totalamt

driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()



#explicit wait - applies to specific element

wait = WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[text()='Code applied ..!']")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

#getting the total amount after discount( after discount value has a decimal value so using float)
discounted_amount = float(driver.find_element(By.XPATH,'//span[@class="discountAmt"]').text)
assert totalamt > discounted_amount

driver.find_element(By.XPATH,"//button[text() = 'Place Order']").click()

driver.find_element(By.XPATH,'//option[@value="India"]').click()
driver.find_element(By.CLASS_NAME,"chkAgree").click()
driver.find_element(By.XPATH,"//button[text() = 'Proceed']").click()

time.sleep(10)

