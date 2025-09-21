from selenium.webdriver.common.by import By
from checkout_confirmation import checkoutconfirmation
class shoppage:

    def __init__(self,driver):
        self.driver = driver
        self.shop_link = (By.XPATH,"//a[contains(@href, 'shop')]")
        self.product_cards = (By.XPATH,'//div[@class="card h-100"]')
        self.checkout_button = (By.XPATH,"//a[contains(text(), 'Checkout')]")

    def add_product_to_cart(self, product_name):

        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productname = product.find_element(By.XPATH,'.//div/h4/a').text
            if productname == product_name:

                product.find_element(By.XPATH,'.//button[@class="btn btn-info"]').click()
            
    def gotocard(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = checkoutconfirmation(self.driver)
        return checkout_confirmation

