from selenium.webdriver.common.by import By

class AuthLocators:
    BUTTON_NO_ACCOUNT = (By.XPATH, ".//button[text()='Нет аккаунта']")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    INPUT_SUBMIT_PASSWORD = (By.NAME, "submitPassword")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, ".//button[text()='Создать аккаунт']")
    RED_BORDER_ELEMENT = (By.XPATH, ".//div[contains(@class,'input_inputError')]")
    INPUT_EMAIL_WITH_ERROR = (By.XPATH, RED_BORDER_ELEMENT[1] + "/input[@name='email']")
    INPUT_PASSWORD_WITH_ERROR = (By.XPATH, RED_BORDER_ELEMENT[1] + "/input[@name='password']")
    INPUT_SUBMIT_PASSWORD_WITH_ERROR = (By.XPATH, RED_BORDER_ELEMENT[1] + "/input[@name='submitPassword']")
    ERROR_TEXT = (By.XPATH, RED_BORDER_ELEMENT[1] + "/ancestor::div/span[text()='Ошибка']")
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    HEADER_NEED_LOGIN = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    