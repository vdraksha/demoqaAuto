import time

import allure
import requests

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    BrokenLinksPage


@allure.suite("Elements Page")
class TestElements:
    URL = "https://demoqa.com/elements"

    @allure.feature("TextBox")
    class TestTextBox:
        URL = "https://demoqa.com/text-box"

        @allure.title('Тест TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, self.URL)
            text_box_page.open_url()

            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "Введённые данные не совпадают с выводом"

    @allure.feature("CheckBox")
    class TestCheckBox:
        URL = "https://demoqa.com/checkbox"

        @allure.title('Тест случайных CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, self.URL)
            check_box_page.open_url()

            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_data = check_box_page.get_checked_checkbox()
            output_data = check_box_page.get_output_item()
            assert input_data == output_data, "check_box не совпадают"

    @allure.feature("RadioButton")
    class TestRadioButton:
        URL = "https://demoqa.com/radio-button"

        @allure.title('Тест случайного RadioButton')
        def test_one_random_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, self.URL)
            radio_button_page.open_url()

            input_data = radio_button_page.click_random_radio_button()
            assert radio_button_page.get_selected_button_output() == input_data, f"radio_button '{input_data}' " \
                                                                                 f"не была выбрана"

        @allure.title('Тест всех RadioButton')
        def test_all_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, self.URL)
            radio_button_page.open_url()
            buttons = ["Yes", "Impressive", "No"]

            radio_button_page.click_radio_button(buttons[0])
            output_data = radio_button_page.get_selected_button_output()
            assert output_data == buttons[0], f"radio_button '{buttons[0]}' не была выбрана"

            radio_button_page.click_radio_button(buttons[1])
            output_data = radio_button_page.get_selected_button_output()
            assert output_data == buttons[1], f"radio_button '{buttons[1]}' не была выбрана"

            radio_button_page.click_radio_button(buttons[2])
            output_data = radio_button_page.get_selected_button_output()
            assert output_data == buttons[2], f"radio_button '{buttons[2]}' не была выбрана"

    @allure.feature("WebTable")
    class TestWebTable:
        URL = "https://demoqa.com/webtables"

        @allure.title('Тест добавления в WebTable')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, self.URL)
            web_table_page.open_url()

            web_table_page.click_add_button()
            input_data = web_table_page.fill_all_fields()
            web_table_page.click_submit_button()

            output_data = web_table_page.collect_table_data()
            assert input_data in output_data, "Данные в таблице не совпадают с введенными"

        @allure.title('Тест поиска в WebTable')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, self.URL)
            web_table_page.open_url()

            keyword = web_table_page.select_random_element()
            web_table_page.fill_search_field(keyword)

            search_data_tabel = web_table_page.collect_table_data(mode='not empty')
            for row in search_data_tabel:
                flag = False
                for cell in row:
                    if keyword in cell:
                        flag = True
                        break
                assert flag, f"Поисковое слово не было найдено в строке {row}"

        @allure.title('Тест редактирования в WebTable')
        def test_web_table_edit_person(self, driver):
            web_table_page = WebTablePage(driver, self.URL)
            web_table_page.open_url()

            keyword = web_table_page.select_random_element()
            web_table_page.fill_search_field(keyword)

            web_table_page.click_edit_button()
            key = web_table_page.fill_one_field()
            web_table_page.click_submit_button()

            all_data_tabel = web_table_page.collect_table_data(mode='not empty')
            assert key in all_data_tabel[0], f"Строка не была изменена или искомая ячейка '{keyword}' была изменена"

        @allure.title('Тест удаления в WebTable')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, self.URL)
            web_table_page.open_url()

            keyword = web_table_page.select_random_element()
            web_table_page.fill_search_field(keyword)
            count_rows = web_table_page.collect_table_data(mode='not empty')

            web_table_page.click_delete_button()

            new_count_rows = web_table_page.collect_table_data(mode='not empty')
            assert len(new_count_rows) < len(count_rows), "Длина списка после удаления строки не изменилась"

        @allure.title('Тест выбора количества отображаемых строк в WebTable')
        def test_web_table_rows_selection(self, driver):
            web_table_page = WebTablePage(driver, self.URL)
            web_table_page.open_url()

            input_data, output_data = web_table_page.click_all_option_rows()

            assert output_data == input_data, f"Не удалось нажать на элемент"

        @allure.title('Тест выбора перелистывания страницы в WebTable')
        def test_web_table_page_selection(self, driver):
            web_table_page = WebTablePage(driver, self.URL)
            web_table_page.open_url()

            output_data = web_table_page.collect_table_data(mode='not empty')
            input_data = [] + output_data + web_table_page.fill_table_data(25)

            web_table_page.click_next_button()
            output_data = web_table_page.collect_table_data(mode='not empty')
            assert output_data == input_data[10:20], "Данные на странице и ожидаемые ожидаемые для страницы " \
                                                     "не совпадают"

            web_table_page.click_previous_button()
            output_data = web_table_page.collect_table_data(mode='not empty')
            assert output_data == input_data[:10], "Данные на странице и ожидаемые ожидаемые для страницы " \
                                                   "не совпадают"

    @allure.feature("Buttons")
    class TestButtons:
        URL = "https://demoqa.com/buttons"

        @allure.title("Тест нажатия кнопок для Buttons")
        def test_pressing_buttons(self, driver):
            buttons_page = ButtonsPage(driver, self.URL)
            buttons_page.open_url()

            buttons_page.double_click_me()
            buttons_page.right_click_me()
            buttons_page.dynamic_click()

            output_data = buttons_page.get_labels()

            assert output_data == ['double', 'right', 'dynamic'], "Не удалось нажать на кнопку"

    @allure.feature("Links")
    class TestLinks:
        URL = "https://demoqa.com/links"

        @allure.title("Тест работы ссылок 'Home' для Links")
        def test_home_links(self, driver):
            links_page = LinksPage(driver, self.URL)
            links_page.open_url()

            url, flag = links_page.check_home_link("simple")
            assert url == "https://demoqa.com/", "Адрес страницы не совпал с ожидаемым"
            assert flag, "По указанному адресу расположена другая страница"

            links_page.close_current_tab()
            links_page.switch_to_tab(0)

            url, flag = links_page.check_home_link("dynamic")
            assert url == "https://demoqa.com/", "Адрес страницы не совпал с ожидаемым"
            assert flag, "По указанному адресу расположена другая страница"

        @allure.title("Тест работы API-запросов для Links")
        def test_api_links(self, driver):
            call_list = ["created", "no-content", "moved",
                         "bad-request", "unauthorized", "forbidden",
                         "invalid-url"]

            links_page = LinksPage(driver, self.URL)
            links_page.open_url()

            for call_name in call_list:
                input_code, output_code = links_page.check_api_link(call_name)
                assert input_code == output_code, f"Не правильный ответ сервера для {call_name}"
                links_page.refresh_page()

    @allure.feature("Broken Links")
    class TestBrokenLinks:
        URL = "https://demoqa.com/broken"

        @allure.title("Тест валидации изображения для Broken Links")
        def test_valid_image(self, driver):
            valid_image = requests.get("https://demoqa.com/images/Toolsqa.jpg").content

            broken_links_page = BrokenLinksPage(driver, self.URL)
            broken_links_page.open_url()

            current_img, element = broken_links_page.get_img()
            assert hash(current_img) == hash(valid_image), f"Картинка ({element}) не соответствует ожидаемой"






