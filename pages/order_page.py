import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def set_name_input(self, name='Акакий'):
        name_input = self.wait_and_find_element(OrderPageLocators.NAME_INPUT_FIELD)
        name_input.send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_second_name_input(self, second_name='Петров'):
        second_name_input = self.wait_and_find_element(OrderPageLocators.SECOND_NAME_INPUT_FIELD)
        second_name_input.send_keys(second_name)

    @allure.step('Заполняем поле Адрес')
    def set_adress_input(self, adress='Улица Почтовая'):
        adress_input = self.wait_and_find_element(OrderPageLocators.ADRESS_INPUT_FIELD)
        adress_input.send_keys(adress)

    @allure.step('Находим поле Метро')
    def metro_field(self):
        self.wait_and_find_element(OrderPageLocators.METRO_STATION_INPUT_FILED).click()

    @allure.step('Выбираем станцию метро')
    def choose_station(self):
        self.wait_and_find_element(OrderPageLocators.METRO_STATION_PICK_EXAMPLE).click()

    @allure.step('Заполняем поле Номер')
    def set_phone_input(self, phone='12345678999'):
        phone_input = self.wait_and_find_element(OrderPageLocators.PHONE_NUMBER_INPUT_FIELD)
        phone_input.send_keys(phone)

    @allure.step('Нажать кнопку Далее')
    def continue_button_click(self):
        self.wait_and_find_element(OrderPageLocators.CONTINUE_BUTTON).click()

    @allure.step('Заполняем поле выбора даты')
    def pick_a_date_input(self):
        self.wait_and_find_element(OrderPageLocators.DATE_PICKER_INPUT_FIELD).click()
        self.wait_and_find_element(OrderPageLocators.DATE_PICKER_CHOOSE_DATE).click()

    @allure.step('Заполняем поле срока аренды')
    def pick_a_duration(self):
        self.wait_and_find_element(OrderPageLocators.DURATION_INPUT_FIELD).click()
        self.wait_and_find_element(OrderPageLocators.DURATION_DROPDOWN_PICK).click()

    @allure.step('Подтверждаем заказ')
    def order_confirmation(self):
        self.wait_and_find_element(OrderPageLocators.CONTINUE_BUTTON).click()
        self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRM_BUTTON).click()

    @allure.step('Находим текст в окне с подтвержденным заказом')
    def order_confirmed(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRMATION_TABLE)
        return True




