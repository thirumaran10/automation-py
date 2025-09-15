from selenium import webdriver   
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,'//div[@class="tox-icon"]').click()
#the text area is inside the frame, so we need to switch to the frame first
driver.switch_to.frame("mce_0_ifr")

editor = driver.find_element(By.XPATH,"//body[@id='tinymce']")
# clear old text (Ctrl+A + Delete)
editor.send_keys("a")
editor.send_keys()

# type new text
editor.send_keys("I am able to automate frames")
time.sleep(10)
'''
driver.find_element(By.ID,"tinymce").clear() #clear the existing text
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")

driver.focus is already inside the frame, so to come out of the frame we need to switch back to default content
driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(5)
'''