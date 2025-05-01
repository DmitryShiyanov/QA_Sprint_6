import allure
import pytest
from data import Constants
from locators.main_page_locators import MainPageLocators
from page_objects.order_page import OrderPage


@allure.title('Тесты на проверку заполнения формы заказа')
@allure.description('Параметризованный тест')
class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_UP, Constants.order_data_1),
            (MainPageLocators.ORDER_BUTTON_DOWN, Constants.order_data_2)
        ]
    )
    def test_order_create(self, driver, main_page, locator, order_data):
        main_page.scroll_to_element(locator)
        main_page.click_to_element(locator)
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        assert 'Заказ оформлен' in order_page.check_order()
