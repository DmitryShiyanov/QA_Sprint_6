from selenium.webdriver.common.by import By


class RedirectPageLocators:
    SAMOKAT_BUTTON = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    DZEN_LOCATOR_FIND = (By.XPATH, "//button[contains(@class, 'arrow__button') and text()='Найти']")
    NEWS_BUTTON = (By.XPATH, "//div[contains(@class, 'dzen-desktop--floor-title__title-2v') and text()='Новости']")
    MAIN_PAGE_TEXT = (By.XPATH, "//div[contains(@class, 'Home_Header__iJKdX') and text()='Самокат на пару дней']")