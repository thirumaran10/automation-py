#java/javascript popup alert using selenium

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#giving a variable to store name
name = "mahadev"
driver.find_element(By.NAME,"enter-name").send_keys(name)
time.sleep(2)
driver.find_element(By.XPATH,'//input[@value="Alert"]').click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(5)

#verifies that the name (mahadev) is present in the alert text.
assert name in alert_text 
alert.accept()#Clicks OK on the alert

#Clicks Cancel on the alert
#alert.dismiss()
time.sleep(5)
