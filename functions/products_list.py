#listing products and adding to cart
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []
driver = webdriver.Chrome()
driver.implicitly_wait(5) #implicit wait - applies to all the elements
driver.get("https://rahulshettyacademy.com/seleniumPractise/?utm_source=chatgpt.com#/")
driver.maximize_window()

driver.find_element(By.XPATH,'//input[@type="search"]').send_keys("ber")
time.sleep(5)

#plural form - to get multiple elements, to get the add to cart button
# get all product cards
products = driver.find_elements(By.XPATH, '//div[@class="products"]/div')

for p in products:
    # get product name inside this card
    name = p.find_element(By.XPATH, './h4[@class="product-name"]').text
    actuallist.append(name)

    # click the add-to-cart button inside this card
    p.find_element(By.XPATH, './div/button').click()
time.sleep(5)
print(actuallist)

driver.find_element(By.XPATH,'//img[@alt="Cart"]').click()
driver.find_element(By.XPATH,"//button[text() = 'PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

#explicit wait - applies to specific element
wait = WebDriverWait(driver,20)
wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Code applied ..!']")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

driver.find_element(By.XPATH,"//button[text() = 'Place Order']").click()

driver.find_element(By.XPATH,'//option[@value="India"]').click()
driver.find_element(By.CLASS_NAME,"chkAgree").click()
driver.find_element(By.XPATH,"//button[text() = 'Proceed']").click()

time.sleep(5)
