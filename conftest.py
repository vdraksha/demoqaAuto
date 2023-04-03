import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function')
def chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def firefox_driver():
    driver = webdriver.firefox(GeckoDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
