
from selenium.webdriver.common.by import By
from pytest_cases.shop import shoppage


#using browserutils without even declaration we have the parent method here, using inheritance
class loginpage():#class loginpage(browserutils):
    def __init__(self, driver):
        #super().__init__(driver)

        self.driver = driver
        self.username_input = (By.ID,"username")
        self.password_input = (By.NAME,"password")
        self.sigin_button = (By.ID,"signInBtn")

    
    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password_input).send_keys("learning")
        self.driver.find_element(*self.sigin_button).click()

        #shop_page = shoppage(self.driver)
        #return shop_page

    