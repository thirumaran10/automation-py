#chrome options and importance of them in selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

'''providing a sepcifc instructions how browser should behave when it get invoked
(before opening the browser the instructions should be given)'''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

print(driver.title)