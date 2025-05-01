import allure

from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage

@allure.title('Класс главной страницы')
class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, number):
        locator_meth_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, number)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_meth_formatted)

    @allure.step('Получение ответа')
    def get_answer_text(self, number):
        locator_mith_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, number)
        return self.get_field_text(locator_mith_formatted)

    @allure.step('Проверяем текст ответа')
    def check_answer_text(self, number):
        self.click_to_question(number)
        return self.get_answer_text(number)
