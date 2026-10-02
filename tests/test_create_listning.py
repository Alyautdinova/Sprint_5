from locators.header_locators import HeaderLocators
from locators.auth_locators import AuthLocators
from locators.listning_locators import ListningLocators
from locators.profile_locators import ProfileLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.webdriver import WebDriver
import random

class TestCreateListing:

    #тест по размещению объявления анонимом
    def test_create_listning_without_login(self, googleDriver: WebDriver):
        googleDriver.get("https://qa-desk.education-services.ru/")

        #нажатие на кнопку Разместить объявление
        googleDriver.find_element(*HeaderLocators.BUTTON_CREATE_LISTNING).click()

        #проверка что отображается текст Чтобы разместить объявление, авторизуйтесь
        header_element = WebDriverWait(googleDriver, 10).until(expected_conditions.visibility_of_element_located(AuthLocators.HEADER_NEED_LOGIN))
        assert header_element.is_displayed()

        googleDriver.quit()

    #тест по размещению объявления авторизованным
    def test_create_listning_with_login(self, googleDriver: WebDriver):
        email = f"user_{random.randint(0, 111)}@example.com"
        password = "Test1909;"
        listning_name = "Тестовое объяление"
        price = 5000

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

        #убеждаемся что пользователь авторизован
        WebDriverWait(googleDriver, 10).until( expected_conditions.visibility_of_element_located(HeaderLocators.BUTTON_AVATAR))

        #ждет появление кнопки "Разместить объявление" и нажимает ее 
        button_create_listing = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_CREATE_LISTNING))
        button_create_listing.click()

        #заполнение полей: «Название», «Описание товара», «Стоимость»
        googleDriver.find_element(*ListningLocators.INPUT_LISTNING_NAME).send_keys(listning_name)
        googleDriver.find_element(*ListningLocators.TEXTAREA_DESCRIPTION).send_keys("Тестовое описание")
        googleDriver.find_element(*ListningLocators.INPUT_PRICE).send_keys(price)

        #выбор города Казань
        googleDriver.find_element(*ListningLocators.ARROW_CITY).click()
        city_option = WebDriverWait(googleDriver, 10).until(expected_conditions.element_to_be_clickable(ListningLocators.CITY_KAZAN_OPTION))
        city_option.click()

        #выбор категории книги
        googleDriver.find_element(*ListningLocators.ARROW_CATEGORY).click()
        category_option = WebDriverWait(googleDriver, 10).until(expected_conditions.element_to_be_clickable(ListningLocators.CATEGORY_BOOK_OPTION))
        category_option.click()

        #нажатие на радио-баттон б/у
        radio_element = googleDriver.find_element(*ListningLocators.RADIOBUTTON_NOT_NEW)
        googleDriver.execute_script("arguments[0].click();", radio_element)

        #нажатие на кнопку "Опубликовать"
        googleDriver.find_element(*ListningLocators.BUTTON_PUBLICATE).click()

        #ждет появление кнопки аватарки и нажимает ее 
        button_avatar = WebDriverWait(googleDriver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_AVATAR))
        button_avatar.click()

        #проверка что перешли на страницу Профиля
        assert googleDriver.current_url == "https://qa-desk.education-services.ru/profile"

        #проверка что карточка с заданными параметрами создалась
        listning_name_element = WebDriverWait(googleDriver, 10).until(expected_conditions.visibility_of_element_located(ProfileLocators.LISTNING_NAME))
        assert listning_name_element.text == "listning_name"
        assert googleDriver.find_element(*ProfileLocators.LISTNING_CITY).text == "Казань"
        assert googleDriver.find_element(*ProfileLocators.LISTNING_PRICE).text == str(price)

        googleDriver.quit()
