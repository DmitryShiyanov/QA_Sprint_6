import allure
import pytest
from selenium import webdriver
from data import Constants
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage

@allure.step('Инициализация драйвера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.step('Инициализация драйвера главной страницы')
@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(Constants.MAIN_PAGE_URL)
    return page

@allure.step('Инициализация драйвера страницы заказа')
@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.go_to_url(Constants.ORDER_PAGE_URL)
    return page
