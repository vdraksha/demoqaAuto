import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'ya.ru')
    page.open_url()
    time.sleep(3)

"""
Запусти test и отдебаж! Время разбора провальных тестов! Бугага
"""

