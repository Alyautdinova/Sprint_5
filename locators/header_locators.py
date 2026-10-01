from selenium.webdriver.common.by import By

class HeaderLocators:
    BUTTON_LOGIN_AND_REGISTRATION = (By.XPATH, ".//button[text()='Вход и регистрация']")
    USER_NAME_ELEMENT = (By.XPATH, ".//div[@class='flexRow']//h3[@class='profileText name']")
    BUTTON_LOGOUT = (By.XPATH, ".//button[text()='Выйти']")