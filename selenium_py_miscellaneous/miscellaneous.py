from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

#to import the head and headless mode('webdriver.ChromeOptions()')
 #create object to this class
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("head")
#some page tell connection private hide details
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)#giving argument to run headless mode
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()

#scrolling to maxheight also use the values to scroll
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#to take the screenshot
driver.get_screenshot_as_file("screen.png")
time.sleep(10)