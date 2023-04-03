import time
from pages.base_page import BasePage
from conftest import firefox_driver


def test(driver):
    page = BasePage(firefox_driver, 'ya.ru')
    page.open_url()
    time.sleep(3)

"""
Запусти test и отдебаж! Время разбора провальных тестов! Бугага
"""

