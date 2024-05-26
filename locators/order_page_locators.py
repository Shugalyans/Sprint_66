from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class OrderPageLocators(BasePageLocators):
    NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SECOND_NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADRESS_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT_FILED = (By.XPATH, "//input[@class='select-search__input']")
    METRO_STATION_PICK_EXAMPLE = (By.XPATH, "//button[@value='62']")
    PHONE_NUMBER_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    DATE_PICKER_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_CHOOSE_DATE = (By.XPATH, "//div[@aria-label='Choose воскресенье, 26-е мая 2024 г.']")

    DURATION_INPUT_FIELD = (By.XPATH, "//div[@class='Dropdown-control']")
    DURATION_DROPDOWN_PICK = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")

    ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    ORDER_CONFIRMATION_TABLE = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")