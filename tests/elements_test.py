import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open_url()
            input_data = text_box_page.fill_all_fields()  # full_name, email, current_address, permanent_address
            output_data = text_box_page.check_filled_form()  # full_name, etc. с поля вывода
            assert input_data == output_data  # Если сравнивать каждое поле отдельно, то локализовать ошибку легче
