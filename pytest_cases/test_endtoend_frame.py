#Selecting a product from list of products with product name parameter

import time

from shop import shoppage

def test_e2e(browserinstance):
    driver = browserinstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    shop_page = shoppage(driver)
    shop_page.add_product_to_cart("Blackberry")
    checkoutconfirmation = shop_page.gotocard()
    checkoutconfirmation.checkout()
    checkoutconfirmation.enter_delivery_address("India")
    checkoutconfirmation.validate_order()
    
    driver.save_screenshot(r"T:\vscode\python_selenium\screenshots\after_checkout.png")
    time.sleep(10)

    driver.close()