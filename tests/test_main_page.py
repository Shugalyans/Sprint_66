import allure
import pytest
import data
from pages.main_page import MainPage
from data import answers


class TestMainPageQuestions:
    @allure.title('Проверка ответов соответствующим открываемым вопросам')
    @allure.description('Через метод параметризации поочередно проверяем соответствие текста ответов вопросам')
    @pytest.mark.parametrize('question', answers)
    def test_click_and_get_answer(self, driver, question):
        number, question = question
        main_page = MainPage(driver)
        main_page.cookie_click()
        main_page.scroll_to_element()
        main_page.wait_for_element_appears()
        main_page.click_and_get_answer(number)
        assert main_page.click_and_get_answer(number).text == question


class TestMainPageTransitions:
    @allure.title('Проверка перехода на главную страницу после нажатия на лого Самоката')
    @allure.description('Переходим на страницу заказа, после чего возвращаемся обратно на главную')
    def test_transition_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.order_upper_button_click()
        main_page.scooter_logo_button_click()
        assert main_page.get_current_url() == data.URL

    @allure.title('Проверка перехода на страницу Дзена после нажатия на лого Яндекса')
    @allure.description('Нажимаем на лого Яндекса и проверяем, что новое окно — Яндекс Дзен')
    def test_transition_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.cookie_click()
        main_page.yandex_logo_button_click()
        main_page.switch_driver()
        main_page.wait_for_title()
        assert '/dzen' in main_page.get_current_url()





