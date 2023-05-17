import os.path
import random
import allure
import requests
from selenium.common import TimeoutException, ElementClickInterceptedException
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, BrokenLinksPageLocators, UpDownloadPageLocators, \
    DynamicPropertiesPageLocator
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """Хранит действия для страницы https://demoqa.com/text-box
    """
    locators = TextBoxPageLocators()

    @allure.step("Заполнение полей")
    def fill_all_fields(self):
        """Вызывает генерацию данных и ими заполняет поля.
        :return: Возвращает сгенерированные данные.
        """
        with allure.step("Генерация пользователя"):
            person_info = next(generated_person())
            full_name = person_info.full_name
            email = person_info.email
            current_address = person_info.current_address
            permanent_address = person_info.permanent_address
        with allure.step("Заполнение полей"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step("Нажатие на кнопку Submit"):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Сбор данных из формы вывода")
    def check_filled_form(self):
        """Собирает данные, которые записаны в полях.
        :return: Возвращает собранные данные.
        """
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    """Хранит действия для страницы https://demoqa.com/checkbox
    """
    locators = CheckBoxPageLocators()

    @allure.step("Нажатие на кнопку (+)")
    def open_full_list(self):
        """Открывает полный список элементов по нажатию на кнопку(+).
        """
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("Нажатие на случайно выбранные чек-боксы")
    def click_random_checkbox(self):
        """В случайном порядке нажимает на чек-боксы, из списка item_list, count раз.
        """
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, 16)]
            if count > 0:
                self.go_to_element(item)
                with allure.step("Нажатие на элемент"):
                    item.click()
                count -= 1
            else:
                break

    @allure.step("Сбор названий выбранных чек-боксов")
    def get_checked_checkbox(self):
        """Собирает список из названий отмеченных чек-боксов, просматривая сами чек-боксы.
        :return: Возвращает отредактированный список.
        """
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        item_list = []
        for box in checked_list:
            title_item = box.find_element('xpath', self.locators.TITLE_ITEM)
            item_list.append(title_item.text)
        return [item.lower().removesuffix('.doc').replace(' ', '') for item in item_list]

    @allure.step("Сбор данных из формы вывода")
    def get_output_item(self):
        """Собирает список из названий отмеченных чек-боксов, просматривая элемент
           страницы со списком отмеченных чек-боксов.
        :return: Возвращает отредактированный список.
        """
        output_list = self.element_are_present(self.locators.OUTPUT_ITEM)
        item_list = []
        for item in output_list:
            item_list.append(item.text)
        return [item.lower() for item in item_list]


class RadioButtonPage(BasePage):
    """Хранит действия для страницы https://demoqa.com/radio-button
    """
    locators = RadioButtonPageLocators()

    @allure.step("Нажатие на случайно выбранную кнопку")
    def click_random_radio_button(self):
        """Нажимает на одну из трёх кнопок, выбранную случайно.
        :return: Возвращает название выбранной кнопки.
        """
        button_list = self.element_are_visible(self.locators.CONTROL_INPUT)
        button = button_list[random.randint(0, 2)]
        with allure.step("Нажатие на элемент"):
            button.click()
        return button.text

    @allure.step("Сбор данных из формы вывода")
    def get_selected_button_output(self):
        """
        :return: Возвращает текст из поля "You have selected"
        """
        try:
            return self.element_is_present(self.locators.SELECTED_BUTTON_OUTPUT).text
        except TimeoutException:
            return None

    @allure.step("Нажатие на выбранную кнопку")
    def click_radio_button(self, button):
        """Нажимает на одну из трёх кнопок, выбранную в button
        :param button: Принимает ключ для словаря radio_buttons
        """
        radio_buttons = {"Yes": self.locators.YES_RADIO,
                         "No": self.locators.NO_RADIO,
                         "Impressive": self.locators.IMP_RADIO}

        self.element_is_visible(radio_buttons[button]).click()


class WebTablePage(BasePage):
    """Хранит действия для страницы "https://demoqa.com/webtables"
    """
    locators = WebTablePageLocators()

    @allure.step("Нажатие на кнопку Add")
    def click_add_button(self):
        """Нажимает на кнопку "Add" на странице.
        """
        self.element_is_visible(self.locators.ADD_BUTTON).click()

    @allure.step("Нажатие на кнопку Edit")
    def click_edit_button(self):
        """Нажимает на кнопку "Edit" на странице.
        """
        self.element_is_visible(self.locators.EDIT_BUTTON).click()

    @allure.step("Нажатие на кнопку Delete")
    def click_delete_button(self):
        """Нажимает кнопку "Delete" на странице
        """
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step("Нажатие на кнопку Submit")
    def click_submit_button(self):
        """Нажимает на кнопку "Submit" в "Registration Form".
        """
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure.step("Раскрытие выпадающего списка")
    def click_rows_selection(self):
        """Нажимает на кнопку выбора количества строк.
        """
        select_button = self.element_is_visible(self.locators.SELECT_ROW_BUTTON)
        self.go_to_element(select_button)
        with allure.step("Нажатие на элемент"):
            select_button.click()

    @allure.step("Нажатие на кнопку Next")
    def click_next_button(self):
        """Переходит к кнопке 'Next' на странице и нажимает на неё.
        """
        next_button = self.element_is_visible(self.locators.NEXT_BUTTON)
        self.go_to_element(next_button)
        button = next_button.find_element("class name", "-btn")
        self.click_element(button)

    @allure.step("Нажатие на кнопку Previous")
    def click_previous_button(self):
        """Переходит к кнопке 'Previous' на странице и нажимает на неё.
        """
        prev_button = self.element_is_visible(self.locators.PREVIOUS_BUTTON)
        self.go_to_element(prev_button)
        button = prev_button.find_element("class name", "-btn")
        self.click_element(button)

    @allure.step("Выбор количества строк")
    def click_all_option_rows(self):
        """Перебирает все варианты отображения количества строк.
        :return: Возвращает список выбранного количества строк.
        """
        row_list = self.element_are_present(self.locators.ROW_LIST)
        output_data = []
        for item in row_list:
            try:
                self.click_rows_selection()
                output_data.append(item.text)
                with allure.step(f"Нажатие на {output_data[-1]}"):
                    item.click()
            except ElementClickInterceptedException:
                return [item.text for item in row_list], output_data
        return [item.text for item in row_list], output_data

    @allure.step("Заполнение полей Registration Form")
    def fill_all_fields(self):
        """Заполняет все поля в "Registration Form".
        """
        with allure.step("Генерация пользователя"):
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
        with allure.step("Заполнение полей"):
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step("Заполнение одного поля Registration Form")
    def fill_one_field(self, key=None):
        """Заполняет одно выбранное или случайное поле в "Registration Form".
        :param key: Указывает на то, какое поле заполнить. По умолчанию - None, случайный выбор.
        """
        with allure.step("Генерация пользователя"):
            person_info = next(generated_person())
            person_data = {"first_name": [self.locators.FIRST_NAME_INPUT, person_info.first_name],
                           "last_name": [self.locators.LAST_NAME_INPUT, person_info.last_name],
                           "email": [self.locators.EMAIL_INPUT, person_info.email],
                           "age": [self.locators.AGE_INPUT, person_info.age],
                           "salary": [self.locators.SALARY_INPUT, person_info.salary],
                           "department": [self.locators.DEPARTMENT_INPUT, person_info.department]}
        if not key:
            with allure.step("Случайный выбор поля"):
                key = random.choice(list(person_data.keys()))
        with allure.step("Заполнение поля"):
            self.element_is_visible(person_data[key][0]).clear()
            self.element_is_visible(person_data[key][0]).send_keys(person_data[key][1])
        return str(person_data[key][1])

    @allure.step("Сбор данных из таблицы")
    def collect_table_data(self, mode: str | None = ...) -> list:
        """Собирает список данных из таблицы.
        :param mode: 'not empty' - без пустых строк таблицы, None - с пустыми.
        :return: Возвращает список данных.
        """
        table_list = self.element_are_visible(self.locators.PERSON_LIST)
        data = [item.text.split('\n') for item in table_list]
        if mode == 'not empty':
            return [item for item in data if len(item) > 1]
        return data

    @allure.step("Заполнение поля поиска")
    def fill_search_field(self,  keyword):
        """Заполняет строку поиска.
        :param keyword: Поисковое слово.
        """
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    @allure.step("Случайный выбор значения из таблицы")
    def select_random_element(self):
        """Собирает данные из таблицы на странице, выбирает строку, выбирает ячейку.
        :return: Возвращает значение из выбранной ячейки.
        """
        all_data_tabel = self.collect_table_data(mode='not empty')
        data_row = all_data_tabel[random.randint(0, len(all_data_tabel) - 1)]
        keyword = data_row[random.randint(0, len(data_row) - 1)]
        return keyword

    @allure.step("Создание массива данных в таблице")
    def fill_table_data(self, count):
        """Заполняет несколько строк таблицы данными.
        :param count: Определяет количество строк.
        :return: Возвращает список внесенных данных.
        """
        data = []
        while count != 0:
            self.click_add_button()
            item = self.fill_all_fields()
            self.click_submit_button()
            data.append(item)
            count -= 1
        return data


class ButtonsPage(BasePage):
    """Хранит действия для страницы https://demoqa.com/buttons
    """
    locators = ButtonsPageLocators()

    @allure.step('Двойное нажатие на кнопку "Double Click Me"')
    def double_click_me(self):
        """Дважды нажимает на кнопку 'Double Click Me'
        """
        element = self.element_is_visible(self.locators.DOUBLE_CLICK)
        self.double_click(element)

    @allure.step('Нажатие правой кнопкой мыши на кнопку "Right Click Me"')
    def right_click_me(self):
        """Нажимает правой кнопкой мыши на кнопку 'Right Click Me'
        """
        element = self.element_is_visible(self.locators.RIGHT_CLICK)
        self.right_click(element)

    @allure.step('Нажатие на кнопку "Click Me"')
    def dynamic_click(self):
        """Нажимает на кнопку 'Click Me'
        """
        self.element_is_visible(self.locators.DYNAMIC_CLICK).click()

    @allure.step('Получение списка нажатых кнопок')
    def get_labels(self):
        button_list = self.element_are_present(self.locators.LABELS)
        return [item.text.split()[-2] for item in button_list]


class LinksPage(BasePage):
    """Хранит действия для страницы https://demoqa.com/links
    """
    locators = LinksPageLocators()

    @allure.step("Проверка ссылки")
    def check_home_link(self, key):
        """Проверяет указанную (key) ссылку - нажимает на неё, получает url и проводит аутентификацию страницы.
        :param key: Название элемента - указатель на ссылку.
        :return: Возвращает url открывшейся страницы. True - открылась ожидаемая страницы.
        """
        links_dict = {"simple": self.locators.SIMPLE_LINK,
                      "dynamic": self.locators.DYNAMIC_LINK}
        with allure.step("Нажатие на ссылку"):
            self.element_is_visible(links_dict[key]).click()
        self.switch_to_tab(1)
        url = self.get_current_url()
        with allure.step("Аутентификация страницы"):
            try:
                self.element_is_visible(self.locators.BANNER_IMG)
                return url, True
            except TimeoutException:
                return url, False

    @allure.step("Проверка API-запроса")
    def check_api_link(self, call_name):
        """Забирает со страницы код ожидаемого ответа и отправляет call_name запрос.
        :param call_name: Название запроса в url запроса.
        :return: Возвращает ожидаемый и полученный код ответа.
        """
        with allure.step(f"Поиск кода ответа для {call_name}"):
            by, loc = self.locators.API_LINK
            self.element_is_visible((by, loc.replace('!replace_this!', call_name))).click()
            response_code = self.element_is_visible(self.locators.RESPONSE_CODE).text
        with allure.step(f"Отправка запроса для {call_name}"):
            response = requests.get(f"https://demoqa.com/{call_name}")
        return int(response_code), response.status_code


class BrokenLinksPage(BasePage):
    """Хранит действия для страницы https://demoqa.com/broken
    """
    locators = BrokenLinksPageLocators()

    @allure.step("Получение изображения и пути к нему")
    def get_img(self):
        """Получает путь к изображению.
        :return: Возвращает байтовое представление, если по полученному пути лежит изображение.
                 Иначе возвращает содержание ответа.
                 Возвращает путь до элемента.
        """
        element = self.element_is_visible(self.locators.BROKEN_IMG).get_attribute("src")
        return requests.get(element).content, element


class UpDownloadPage(BasePage):
    """Хранить действия для страницы https://demoqa.com/upload-download
    """
    locators = UpDownloadPageLocators()

    @allure.step("Нажатие на кнопку 'Download'")
    def click_download(self):
        """Нажимает на кнопку 'Download' на странице.
        """
        self.element_is_visible(self.locators.DOWNLOAD_BUTTON).click()

    @allure.step("Проверка наличия загруженного файла")
    def check_download_file(self, path):
        """Забирает имя файла скачиваемого файла и проверяет его наличие в папке загрузки.
        :param path: Путь до папки загрузки.
        :return: Возвращает True, если файл в каталоге. Иначе False.
        """
        file = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute("download")
        return os.path.exists(path + file)

    @allure.step("Выгрузка файла на сервер")
    def set_upload_file(self):
        """Создаёт файл в системе, передает путь до него в input, затем удаляет его из системы.
        :return: Возвращает имя созданного файла.
        """
        path = generated_file()
        self.element_is_present(self.locators.SELECT_FILE_INPUT).send_keys(path)
        os.remove(path)
        return path.split("\\")[-1]

    @allure.step("Получение сведений о файле на сервере")
    def check_upload_file(self):
        """Получает путь, по которому был скачан файл.
        :return: Возвращает имя скачанного файла.
        """
        text = self.element_is_present(self.locators.SELECT_FILE_OUTPUT).text
        return text.split("\\")[-1]


class DynamicPropertiesPage(BasePage):
    """Хранить действия для страницы https://demoqa.com/dynamic-properties
    """
    locators = DynamicPropertiesPageLocator()

    @allure.step("Получение состояния кнопки")
    def check_enable_button(self, timeout):
        """Ожидает указанное время возможности нажать на кнопку.
        :param timeout: Время ожидания.
        :return: Возвращает True, если на кнопку можно нажать. Иначе False.
        """
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_BUTTON, timeout)
        except TimeoutException:
            return False
        return True

    @allure.step("Получение цвета текста кнопки")
    def get_color_button(self, timeout):
        """Получает текст цвета кнопки.
        :param timeout: Время ожидания перед получением цвета.
        :return: Возвращает цвет в формате rgba(0, 0, 0, 0)
        """
        self.driver.implicitly_wait(timeout)
        button = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON, 0.01)
        return button.value_of_css_property("color")

    @allure.step("Получение состояния кнопки")
    def check_visible_button(self, timeout):
        """Ожидает указанное время появление кнопки.
        :param timeout: Время ожидания.
        :return: Возвращает True, если кнопка появилась. Иначе False.
        """
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON, timeout)
        except TimeoutException:
            return False
        return True



