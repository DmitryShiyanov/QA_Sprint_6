import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@allure.title('Базовый класс')
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу с ожиданием')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Метод заполнения поля')
    def add_text_in_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Метод изьятия текста с элемента')
    def get_field_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Метод скролл')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Метод распаковки локатора и форматирования')
    def format_locators(self, locator_1, number):
        method, locator = locator_1
        locator = locator.format(number)
        return (method, locator)

    @allure.step('Метод открытия URL')
    def go_to_url(self, url):
        self.driver.get(url)
