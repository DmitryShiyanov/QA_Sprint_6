from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_PLACEHOLDER = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_PLACEHOLDER = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_PLACEHOLDER = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    TELEPHONE_PLACEHOLDER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    METRO_STATIONS = (By.XPATH, '//*[text()="Сокольники"]')
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Button') and text()='Далее']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    TIME_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TIME_WIDGET = (By.XPATH, "//*[contains(@aria-label, '25-е апреля 2025 г.')]")
    TIME_RENT_FIELD = (By.XPATH, '//*[contains(@class, "Dropdown-placeholder") and text()="* Срок аренды"]')
    ONE_DAY_BUTTON = (By.XPATH, '//*[contains(@class, "Dropdown-option") and text()="сутки"]')
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    ORDER_AGGRY_BTN = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Да']")
    SUCCESS_ORDER = (By.XPATH, '//*[text()="Заказ оформлен"]')
    CHECK_STATUS_BTN = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Посмотреть статус']")