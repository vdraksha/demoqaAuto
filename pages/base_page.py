import allure
from selenium.webdriver import ActionChains
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
        :param element: Принимает ссылку на WebElement.
        """
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step("Нажатие на элемент через JS-скрипт")
    def click_element(self, element):
        """Нажимает на указанный элемент.
        :param element: Принимает ссылку на WebElement.
        """
        self.driver.execute_script('arguments[0].click();', element)

    @allure.step("Двойное нажатие на элемент")
    def double_click(self, element):
        """Совершает двойное нажатие на элемент.
        :param element: Принимает ссылку на WebElement.
        """
        act = ActionChains(self.driver)
        act.move_to_element(element)
        act.double_click(element)
        act.perform()

    @allure.step("Нажатие правой кнопкой мыши на элемент")
    def right_click(self, element):
        """Совершает нажатие правой кнопкой мыши на элемент.
        :param element: Принимает ссылку на WebElement.
        """
        act = ActionChains(self.driver)
        act.move_to_element(element)
        act.context_click(element)
        act.perform()

    @allure.step("Переключение на вкладку")
    def switch_to_tab(self, number):
        """Переключает на выбранную по индексу вкладку.
        :param number: Индекс вкладки.
        """
        self.driver.switch_to.window(self.driver.window_handles[number])

    @allure.step("Получение адреса текущей страницы")
    def get_current_url(self):
        """Получает адрес текущей вкладки.
        :return: Возвращает адрес.
        """
        return self.driver.current_url

    @allure.step("Закрытие текущей вкладки")
    def close_current_tab(self):
        """Закрывает текущую вкладку.
        """
        self.driver.close()

    @allure.step("Обновление страницы")
    def refresh_page(self):
        """Обновляет текущую страницу.
        """
        self.driver.refresh()
