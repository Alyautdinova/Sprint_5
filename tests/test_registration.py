from locators.header_locators import HeaderLocators
from locators.auth_locators import AuthLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.webdriver import WebDriver
from data.urls import Urls
import random

class TestUserRegistration():

    #тест по регистрации пользователя с валидными данными
    def test_registration_successful(self, googleDriver: WebDriver):
        email = f"user_{random.randint(0, 111)}@example.com"
        password = "Test1909;"

        #открытие страницы
        googleDriver.get(Urls.BASE_URL)
        
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
        assert googleDriver.current_url == Urls.REGISTRATION_URL

        #проверка имени юзера
        user_name_element = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.USER_NAME_ELEMENT)).text
        assert user_name_element == "User."

        googleDriver.quit()

    #тест по регистрации пользователя с невалидными email и без пароля
    def test_registration_invalid_email_and_empty_password(self, googleDriver: WebDriver):
        email = f"user_{random.randint(0, 111)}"
    
        #открытие страницы
        googleDriver.get(Urls.BASE_URL)
            
        #нажатие на кнопку "Вход и регистрация"
        googleDriver.find_element(*HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION).click()
    
        #ждет появление кнопки "Нет аккаунта" и нажимает ее
        button_no_account = WebDriverWait(googleDriver, 3).until(expected_conditions.visibility_of_element_located(AuthLocators.BUTTON_NO_ACCOUNT))
        button_no_account.click()
    
        #заполнение формы регистрации - email, пароль и подтверждение пароля
        googleDriver.find_element(*AuthLocators.INPUT_EMAIL).send_keys(email)
            
        #нажатие на кнопку "Создать аккаунт"
        googleDriver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()
    
        #проверка, что отображаются красные границы для полей email, пароль и подтвержение пароля
        input_error_email = WebDriverWait(googleDriver, 3).until(expected_conditions.visibility_of_element_located(AuthLocators.INPUT_EMAIL_WITH_ERROR))
        input_error_email.is_displayed()
        assert googleDriver.find_element(*AuthLocators.INPUT_PASSWORD_WITH_ERROR).is_displayed()
        assert googleDriver.find_element(*AuthLocators.INPUT_SUBMIT_PASSWORD_WITH_ERROR).is_displayed()

        #проверка, что отображается текст с Ошибкой
        assert googleDriver.find_element(*AuthLocators.ERROR_TEXT).is_displayed

        googleDriver.quit()

    #тест по регистрации существующего в системе пользователя
    def test_registration_with_exist_user(self, googleDriver: WebDriver):
        email = f"user_{random.randint(0, 111)}@example.com"
        password = "Test1909;"

        #открытие страницы
        googleDriver.get(Urls.BASE_URL)
        
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

        #проверка имени юзера
        user_name_element = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.USER_NAME_ELEMENT)).text
        assert user_name_element == "User."

        #нажатие на кнопку Выйти
        googleDriver.find_element(*HeaderLocators.BUTTON_LOGOUT).click()

        #повторная попытка регистрации с теми же данными
        button_login_and_registration = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION))
        button_login_and_registration.click()
        button_no_account = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(AuthLocators.BUTTON_NO_ACCOUNT))
        button_no_account.click()
        googleDriver.find_element(*AuthLocators.INPUT_EMAIL).send_keys(email)
        googleDriver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.INPUT_SUBMIT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()

        #проверка, что отображаются красные границы для полей email, пароль и подтвержение пароля
        input_error_email = WebDriverWait(googleDriver, 3).until(expected_conditions.visibility_of_element_located(AuthLocators.INPUT_EMAIL_WITH_ERROR))
        input_error_email.is_displayed()
        assert googleDriver.find_element(*AuthLocators.INPUT_PASSWORD_WITH_ERROR).is_displayed()
        assert googleDriver.find_element(*AuthLocators.INPUT_SUBMIT_PASSWORD_WITH_ERROR).is_displayed()

        #проверка, что отображается текст с Ошибкой
        assert googleDriver.find_element(*AuthLocators.ERROR_TEXT).is_displayed

        googleDriver.quit()
