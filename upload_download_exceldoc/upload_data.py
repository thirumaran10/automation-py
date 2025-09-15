
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from update_data import update_excel_data #importing the function from update file

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()

file_path = "T:\\vscode\\python_selenium\\data\\download.xlsx"#path of the excel file
fruit_name = "Apple"#without hard coding the locator make a dynamic(use in xpath)
newvalue = "999"
driver.find_element(By.ID,"downloadButton").click()


#updated excel file datas
update_excel_data(file_path, "price", fruit_name, newvalue)
#upload
file_input = driver.find_element(By.XPATH,'//input[@type="file"]')
#giving the path of file present in local that has to upload 
file_input.send_keys(file_path)


#explicit wait 
wait = WebDriverWait(driver,10)
toast_locator = (By.XPATH,"//div[contains(text(), 'Updated Excel Data Successfully')]")#locator in a variable
wait.until(EC.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)
'''toast = wait.until(EC.visibility_of_element_located(toast_locator))
print(toast.text)'''

driver.find_element(By.XPATH,"//div[text() = 'Price']").get_attribute('data-column-id')
#'Apple' => '"+fruit_name+"'(#without hard coding the locator make a dynamic(use in xpath))
actual_price = driver.find_element(By.XPATH,"//div[text() = 'Apple']/parent::div/parent::div/div[@id='cell-4-undefined']").text


assert actual_price == newvalue
time.sleep(10)

