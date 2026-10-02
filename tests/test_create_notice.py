from locators.header_locators import HeaderLocators
from locators.auth_locators import AuthLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.webdriver import WebDriver
import random

class TestCreateNotice:

    #тест по размещению объявления анонимом
    def test_create_notice_without_login(self, googleDriver: WebDriver):
        googleDriver.get("https://qa-desk.education-services.ru/")

        #нажатие на кнопку Разместить объявление
        googleDriver.find_element(*HeaderLocators.BUTTON_CREATE_NOTICE).click()

        #проверка что отображается текст Чтобы разместить объявление, авторизуйтесь
        assert googleDriver.find_element(*AuthLocators.HEADER_NEED_LOGIN).is_displayed()

        googleDriver.quit()
