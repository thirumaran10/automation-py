#data should not be part of the page

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class checkoutconfirmation:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH,'//button[@class="btn btn-success"]')
        self.country_input = (By.ID,"country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH,'//label[@for="checkbox2"]')
        self.submit_button = (By.XPATH,'//input[@value="Purchase"]')
        self.success_message = (By.CLASS_NAME,'alert-success')


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryname):
        
        self.driver.find_element(*self.country_input).send_keys(countryname)
        wait = WebDriverWait(self.driver,10) 
        wait.until(expected_conditions.element_to_be_clickable(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def validate_order(self):
        
        success = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in success
    
   
        
    

    
    
    
        