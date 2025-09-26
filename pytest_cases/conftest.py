import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Regester code -we telling the to register the code that waht i send using terminal
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser selection")


#getting the name form terminal using, "--browser" command
@pytest.fixture(scope="function")
def browserinstance(request):
    browser_name = request.config.getoption("--browser")
    service_obj = Service()

    if browser_name == "chrome": #genderliz the browser name
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(5)

    driver.maximize_window()
    yield driver# befor test function execution

    # Teardown
    try:
        driver.quit()   # closes all tabs + ends session
    except Exception:
        pass
    #driver.close()# post your test function execution
    
    '''post function execution - after completing all the test (browser instance)
      came back to this conftest and see if there is any code under the yield 
      because yield told that the code to execute the method first and came last ''' 
    

