from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    URL = "https://demoqa.com/elements"

    class TestTextBox:
        URL = "https://demoqa.com/text-box"

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, self.URL)
            text_box_page.open_url()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data  # Если сравнивать каждое поле отдельно, то локализовать ошибку легче

    class TestCheckBox:
        URL = "https://demoqa.com/checkbox"

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, self.URL)
            check_box_page.open_url()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_data = check_box_page.get_checked_checkbox()
            output_data = check_box_page.get_output_item()
            assert input_data == output_data

