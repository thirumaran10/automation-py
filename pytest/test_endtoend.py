# End to end framework 
#Selecting a product from list of products with product name parameter using pytest (its run using pytest only)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


def test_endtoend(browserinstance):
    driver=browserinstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    

    driver.find_element(By.XPATH,"//a[contains(@href, 'shop')]").click()#using contains attribute
    products = driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

    for product in products:
        productname = product.find_element(By.XPATH,'.//div/h4/a').text
        if productname == "Blackberry":
            product.find_element(By.XPATH,'.//button[@class="btn btn-info"]').click()
            break

    driver.find_element(By.XPATH,"//a[contains(text(), 'Checkout')]").click()
    driver.find_element(By.XPATH,'//button[@class="btn btn-success"]').click()

    driver.find_element(By.ID,"country").send_keys('Ind')

    #explicit wait - applies to specific element
    wait = WebDriverWait(driver,10) 
    india_choice = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'India')))
    india_choice.click()

    driver.find_element(By.XPATH,'//label[@for="checkbox2"]').click()
    driver.find_element(By.XPATH,'//input[@value="Purchase"]').click()

    success = driver.find_element(By.CLASS_NAME,'alert-success').text

    assert "Success! Thank you!" in success
    
    '''== make exact match, in mean the text we mention present compltely in the variable'''
    time.sleep(10)

    
    