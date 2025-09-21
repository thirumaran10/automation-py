import pytest
from selenium import webdriver

# Regester code -we telling the to register the code that waht i send using terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser selection"
    )


#getting the name form terminal using, "--browser" command
@pytest.fixture(scope="function")
def browserinstance(request):
    browser_name = request.config.getoption("browser")


    if browser_name == "chrome": #genderliz the browser name
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver# befor test function execution
    driver.close()# post your test function execution
    '''post function execution - after completing all the test (browser instance)
      came back to this conftest and see if there is any code under the yield 
      because yield told that the code to execute the method first and came last ''' 
    

