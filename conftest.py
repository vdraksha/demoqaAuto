import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    #driver.set_page_load_timeout(30)
    driver.maximize_window()
    yield driver
    driver.quit()
