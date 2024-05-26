from pages.order_page import OrderPage
import allure
import pytest


class TestOrderPage:

    @allure.title('Заполнение формы заказа самоката')
    @allure.description('Заполняем форму заказа самоката, используя две кнопки Заказать как точки входа')
    @pytest.mark.parametrize('order_button', ['order_upper_button_click', 'order_bottom_button_click'])
    def test_order_page(self, driver, order_button):
        order_page = OrderPage(driver)
        order_page.cookie_click()
        order_button_func = getattr(order_page, order_button)
        order_button_func()
        order_page.set_name_input()
        order_page.set_second_name_input()
        order_page.set_adress_input()
        order_page.metro_field()
        order_page.choose_station()
        order_page.set_phone_input()
        order_page.continue_button_click()
        order_page.pick_a_date_input()
        order_page.pick_a_duration()
        order_page.order_confirmation()

        assert order_page.order_confirmed()

