import  time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#Id, xpath, CSS selector, name, link text, partial link text, tag name(locators)
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

#//tagename[@attribute='value'] --> xpath
#tagename[attribute='value'] --> css selector
driver.find_element(By.CSS_SELECTOR,'input[name="name"]').send_keys('kong')
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

driver.find_element(By.XPATH,'//input[@type="submit"]').click()
#menting class name and give variable name and print it
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

#assertion to check if the message contains "success"
assert "success" in message

time.sleep(10)
#in webpage it is a twoway data binding
driver.find_element(By.XPATH,'//input[@class="ng-pristine ng-valid ng-touched"]').send_keys('hello')

#to clear the input field(all)
driver.find_element(By.XPATH,'//input[@class="ng-pristine ng-valid ng-touched"]').clear()
