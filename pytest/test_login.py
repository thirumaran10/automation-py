
import os
import json
import time
import pytest
from selenium import webdriver
from login import loginpage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


# build absolute path to json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_data_path = os.path.join(BASE_DIR, "data", "test_login.json")

# load test data
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_loginpage(test_list_item):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    login = loginpage(driver)
    login.login(test_list_item["userEmail"], test_list_item["userpassword"])

    time.sleep(5)
    driver.quit()
