from selenium import webdriver   
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # to perform mouse actions

from selenium import webdriver 

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.LINK_TEXT,"Click Here")).click().perform()

windos_opened = driver.window_handles#list of all opened windows names

driver.switch_to.window(windos_opened[1])#switch to the new window (index 1) starts from 0
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()#close the child window
time.sleep(10)
driver.switch_to.window(windos_opened[0])#switch back to the main window (index 0)

print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(10)

# ...existing code...
print("Script ran successfully...")