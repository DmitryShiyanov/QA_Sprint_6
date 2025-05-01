import allure
from data import Constants
from page_objects.redirect_page import RedirectPage


@allure.title('Тестирование перехода между страницами')
class TestRedirectPage:

    # @allure.step('Тест перехода по клику на Самокат')
    # def test_navigate_main_case(self, driver, order_page):
    #     redirect_page = RedirectPage(driver)
    #     redirect_page.redirect_main_page()
    #     assert 'Заказать' in redirect_page.check_main_page() and redirect_page.check_url_page() == Constants.MAIN_PAGE_URL

    @allure.step('Тест редиректа на Дзен')
    def test_redirect_to_yandex_dzen(self, main_page, driver):
        redirect = RedirectPage(driver)
        redirect.redirect_to_dzen()
        redirect.wait()
        redirect.switch_to_window()
        assert 'Новости' in redirect.check_dzen_main_page() and redirect.check_url_page().startswith("https://dzen.ru")
