import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open_url()
            text_box_page.fill_all_fields()
            out_full_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_form()
            print(out_full_name)
            print(out_email)
            print(out_current_address)
            print(out_permanent_address)

