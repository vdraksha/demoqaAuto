import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Представление базовой страницы и её методов, которые будут наследовать представления
       других страниц для работы с их элементами.
    """
    def __init__(self, driver, url):
        """Инициализация переменных для открытия страницы.
        :param driver: Вызывает драйвер. Передавать как driver.
        :param url: Адрес страницы.
        """
        self.driver = driver
        self.url = url

    @allure.step("Открытие ссылки")
    def open_url(self):
        """Открытие страницы по url.
        """
        self.driver.get(self.url)

    @allure.step("Поиск элемента")
    def element_is_visible(self, locator, timeout=5):
        """Ожидает загрузку и отображение одного элемента на странице для взаимодействия с ним.
        :param locator: Указание на место элемента в html-документе(xpath, селектор).
        :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Поиск элементов")
    def element_are_visible(self, locator, timeout=5):
        """Ожидает загрузку и отображение нескольких элементов на странице для взаимодействия с ними.
        :param locator: Указание на место элементов в html-документе(xpath, селектор).
        :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Поиск элемента")
    def element_is_present(self, locator, timeout=5):
        """Ожидает загрузку одного элемента в html-документе для взаимодействия с ним. Отображение необязательно.
        :param locator: Указание на место элемента в html-документе(xpath, селектор).
        :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Поиск элементов")
    def element_are_present(self, locator, timeout=5):
        """Ожидает загрузку нескольких элементов в html-документе для взаимодействия с ними. Отображение необязательно.
        :param locator: Указание на место элементов в html-документе(xpath, селектор).
        :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Поиск элемента")
    def element_is_not_visible(self, locator, timeout=5):
        """Ожидание отсутствия элемента.
        :param locator: Указание на место элемента в html-документе(xpath, селектор).
        :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Поиск элемента")
    def element_is_clickable(self, locator, timeout=5):
        """Ожидание отображения элемента для клика по нему.
        :param locator: Указание на место элемента в html-документе(xpath, селектор).
        :param timeout: Время ожидания загрузки. По умолчанию 5 сек.
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Переход к элементу")
    def go_to_element(self, element):
        """Перемещает к указанному элементу на странице.
        arguments[0].scrollIntoView(); - скрипт для перемещения.
        :param element: Указание на место элемента в html-документе(xpath, селектор).
        """
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step("Нажатие на элемент через JS-скрипт")
    def click_element(self, element):
        """Нажимает на указанный элемент.
        :param element: Указание на место элемента в html-документе(xpath, селектор).
        """
        self.driver.execute_script('arguments[0].click();', element)


