from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """Хранит локаторы для элементов страницы https://demoqa.com/text-box
    """
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    """Хранит локаторы для элементов страницы https://demoqa.com/checkbox
    """
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"  # xpath
    OUTPUT_ITEM = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    """Хранит локаторы для элементов страницы https://demoqa.com/radio-button
    """
    CONTROL_INPUT = (By.CSS_SELECTOR, "div[class^='custom-control'] label")
    SELECTED_BUTTON_OUTPUT = (By.CSS_SELECTOR, "p span[class='text-success']")
    YES_RADIO = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMP_RADIO = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[for='noRadio']")
    SUCCESS_TEXT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    """Хранит локаторы для элементов страницы https://demoqa.com/webtables
    """
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    SELECT_ROW_BUTTON = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page'] option[value]")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, "div[class='-previous']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div[class='-next']")

    # Registration Form
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")


class ButtonsPageLocators:
    """Хранит локаторы для элементов страницы https://demoqa.com/buttons
    """
    DOUBLE_CLICK = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    DYNAMIC_CLICK = (By.CSS_SELECTOR, "div[class='mt-4']:nth-child(3) button")
    LABELS = (By.CSS_SELECTOR, "div p[id]")

