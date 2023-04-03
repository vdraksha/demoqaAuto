import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://ya.ru/')
    page.open_url()
    time.sleep(3)

