from selenium.webdriver.common.by import By

class AuthLocators:
    BUTTON_NO_ACCOUNT = (By.XPATH, ".//button[text()='Нет аккаунта']")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    INPUT_SUBMIT_PASSWORD = (By.NAME, "submitPassword")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, ".//button[text()='Создать аккаунт']")
    