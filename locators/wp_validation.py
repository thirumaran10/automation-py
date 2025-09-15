from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
time.sleep(5)
#using the link text locator
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/child::input").send_keys("vinayak50@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Vinayak50_")
#in css just mention the id using- #
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Vinayak50_")
#driver.find_element(By.XPATH,"//button[@type="submit"]").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(2)