from locators.header_locators import HeaderLocators
from locators.auth_locators import AuthLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.webdriver import WebDriver
import random

class TestUserRegistration():

    def test_registration_successful(self, googleDriver: WebDriver):
        email = f"user_{random.randint(0, 111)}@example.com"
        password = "Test1909;"

        #открытие страницы
        googleDriver.get("https://qa-desk.education-services.ru/")
        
        #нажатие на кнопку "Вход и регистрация"
        googleDriver.find_element(*HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION).click()

        #ждет появление кнопки "Нет аккаунта" и нажимает ее
        button_no_account = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(AuthLocators.BUTTON_NO_ACCOUNT))
        button_no_account.click()

        #заполнение формы регистрации - email, пароль и подтверждение пароля
        googleDriver.find_element(*AuthLocators.INPUT_EMAIL).send_keys(email)
        googleDriver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.INPUT_SUBMIT_PASSWORD).send_keys(password)
        
        #нажатие на кнопку "Создать аккаунт"
        googleDriver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()

        #проверка урла
        assert googleDriver.current_url == "https://qa-desk.education-services.ru/regiatration"

        #проверка имени юзера
        user_name_element = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.USER_NAME_ELEMENT)).text
        assert user_name_element == "User."

        googleDriver.quit()
