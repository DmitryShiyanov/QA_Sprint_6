import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.redirect_page_locators import RedirectPageLocators
from page_objects.base_page import BasePage

@allure.title('Класс страницы редиректа')
class RedirectPage(BasePage):

    @allure.step('Клик на кнопку Самокат')
    def redirect_main_page(self):
        self.click_to_element(RedirectPageLocators.SAMOKAT_BUTTON)

    @allure.step('Проверка url')
    def check_url_page(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Метод редиректа на Дзен')
    def redirect_to_dzen(self):
        self.click_to_element(RedirectPageLocators.YANDEX_BUTTON)

    @allure.step('Ожидание')
    def wait (self):
        try:
            WebDriverWait(self.driver, 5).until((expected_conditions.presence_of_element_located(RedirectPageLocators.NEWS_BUTTON)))
        except Exception:
            TimeoutError

    @allure.step('Метод для текста кнопки страницы Дзен')
    def check_dzen_main_page(self):
        return self.get_field_text(RedirectPageLocators.NEWS_BUTTON)

    @allure.step('Метод для текста кнопки главной')
    def check_main_page(self):
        return self.get_field_text(MainPageLocators.ORDER_BUTTON_UP)
