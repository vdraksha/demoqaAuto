import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    """Вызывает драйвер для управления работой браузера на базе выбранного webdriver.
       Декоратор @pytest.fixture позволяет вызвать драйвер в нужном тесте под именем
       driver.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

