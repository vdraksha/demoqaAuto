import pytest
import allure
from datetime import datetime
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    """Вызывает драйвер для управления работой браузера на базе выбранного webdriver.
       Декоратор @pytest.fixture позволяет вызвать драйвер в нужном тесте под именем
       driver.
    """
    options = webdriver.ChromeOptions()
    options.set_capability("pageLoadStrategy", "eager")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot_{datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()

