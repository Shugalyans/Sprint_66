from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators


@allure.step('Вытаскиваем по номеру и возвращаем локаторы вопросов')
def question_locator(number):
    return MainPageLocators.QUESTIONS[number]


@allure.step('Вытаскиваем по номеру и возвращаем локаторы ответов')
def answer_locator(number):
    return MainPageLocators.ANSWERS[number]


class MainPage(BasePage):

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_is('Дзен')

    @allure.step('Ищем вопросы, раскрываем их и фиксируем ответы')
    def click_and_get_answer(self, number):
        self.wait_and_find_element(question_locator(number)).click()
        return self.wait_and_find_element(answer_locator(number))

    @allure.step('Скроллим до нужного элемента')
    def scroll_to_element(self):
        self.scroll(MainPageLocators.QUESTIONS[1])

    @allure.step('Ожидаем появления элемента, до которого скроллили')
    def wait_for_element_appears(self):
        self.wait_and_find_element(MainPageLocators.QUESTIONS[1])

    @allure.step('Нажимаем на кнопку сервиса Самокат вверху страницы')
    def scooter_logo_button_click(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажимаем на кнопку Яндекса вверху страницы')
    def yandex_logo_button_click(self):
        self.click(MainPageLocators.YANDEX_LOGO)
