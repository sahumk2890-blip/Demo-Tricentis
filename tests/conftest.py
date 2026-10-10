import pytest
from selenium import webdriver

'''@pytest.fixture(autouse=True)
def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()'''

@pytest.fixture(params=['chrome','edge','firefox'])
def setup_and_teardown(request):

    browser = request.param
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()


    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()