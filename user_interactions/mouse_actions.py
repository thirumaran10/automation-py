
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains#to perform mouse actions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

#move to particular element
ActionChains(driver).move_to_element(driver.find_element(By.ID,"mousehover")).perform()
ActionChains(driver).context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

time.sleep(5)
'''
ActionChains(driver).click_and_hold #used to longpress
ActionChains(driver).context_click #right click
ActionChains(driver).double_click #double click
ActionChains(driver).drag_and_drop #drag and drop '''

