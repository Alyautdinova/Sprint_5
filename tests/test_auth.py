from locators.header_locators import HeaderLocators
from locators.auth_locators import AuthLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.webdriver import WebDriver
import random

class TestAuth:

    #тест на вход под существующим в системе пользователем
    def test_login_with_exist_user(self, googleDriver: WebDriver):
        email = f"user_{random.randint(0, 111)}@example.com"
        password = "Test1909;"

        #регистрация пользователя
        googleDriver.get("https://qa-desk.education-services.ru/")
        googleDriver.find_element(*HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION).click()
        button_no_account = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(AuthLocators.BUTTON_NO_ACCOUNT))
        button_no_account.click()
        WebDriverWait(googleDriver, 10).until(expected_conditions.visibility_of_element_located(AuthLocators.INPUT_EMAIL))
        googleDriver.find_element(*AuthLocators.INPUT_EMAIL).send_keys(email)
        googleDriver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.INPUT_SUBMIT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()

        #ждет появление кнопки "Выйти" и нажимает ее
        button_logout = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_LOGOUT))
        button_logout.click()

        #вход под зарегистрированным пользователем
        button_login_and_registration = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION))
        button_login_and_registration.click()
        googleDriver.find_element(*AuthLocators.INPUT_EMAIL).send_keys(email)
        googleDriver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.BUTTON_LOGIN).click()

        #проверка урла
        assert googleDriver.current_url == "https://qa-desk.education-services.ru/login"

        #проверка имени юзера
        user_name_element = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.USER_NAME_ELEMENT)).text
        assert user_name_element == "User."

        #проверка отображения аватарки
        assert googleDriver.find_element(*HeaderLocators.BUTTON_AVATAR).is_displayed()

        googleDriver.quit()

    #тест на выход
    def test_logout(self, googleDriver: WebDriver):
        email = f"user_{random.randint(0, 111)}@example.com"
        password = "Test1909;"

        #регистрация пользователя
        googleDriver.get("https://qa-desk.education-services.ru/")
        googleDriver.find_element(*HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION).click()
        button_no_account = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(AuthLocators.BUTTON_NO_ACCOUNT))
        button_no_account.click()
        googleDriver.find_element(*AuthLocators.INPUT_EMAIL).send_keys(email)
        googleDriver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.INPUT_SUBMIT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()

        #ждет появление кнопки "Выйти" и нажимает ее
        button_logout = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_LOGOUT))
        button_logout.click()

        #вход под зарегистрированным пользователем
        button_login_and_registration = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION))
        button_login_and_registration.click()
        googleDriver.find_element(*AuthLocators.INPUT_EMAIL).send_keys(email)
        googleDriver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(password)
        googleDriver.find_element(*AuthLocators.BUTTON_LOGIN).click()

        #проверка отображения кнопки Вход и регистрация
        assert googleDriver.find_element(*HeaderLocators.BUTTON_LOGIN_AND_REGISTRATION).is_displayed()

        #проверка что имя юзера не отображается
        assert WebDriverWait(googleDriver, 3).until(expected_conditions.invisibility_of_element(HeaderLocators.USER_NAME_ELEMENT))

        #проверка что аватарка не отображается
        assert len(googleDriver.find_elements(*HeaderLocators.BUTTON_AVATAR)) == 0

        googleDriver.quit()
