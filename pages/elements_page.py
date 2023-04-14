import random
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """Хранит тесты для страницы https://demoqa.com/text-box
    """
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """Вызывает генерацию данных и ими заполняет поля.
        :return: Возвращает сгенерированные данные.
        """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

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
    """Хранит тесты для страницы https://demoqa.com/checkbox
    """
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        """Открывает полный список элементов по нажатию на кнопку(+).
        """
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """В случайном порядке нажимает на чек-боксы, из списка item_list, count раз.
        """
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, 16)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

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





