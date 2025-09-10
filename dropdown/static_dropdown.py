#Static dropdowns of using select class of selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
#to import select class
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,'input[name="name"]').send_keys('vinayak')
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

#static dropdown - when we have fixed set of values
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)
#also we can use value - dropdown.select_by_value()

driver.find_element(By.XPATH,'//input[@type="submit"]').click()

time.sleep(5)