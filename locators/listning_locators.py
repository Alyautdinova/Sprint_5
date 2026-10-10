from selenium.webdriver.common.by import By

class ListningLocators:
    INPUT_LISTNING_NAME = (By.NAME, "name")
    RADIOBUTTON_NEW = (By.XPATH, ".//div[contains(@class, 'radioUnput')]/input[@value='Новый']")
    RADIOBUTTON_NOT_NEW = (By.XPATH, ".//div[contains(@class, 'radioUnput')]/input[@value='Б/У']")
    ARROW_CITY = (By.XPATH, ".//input[@name='city']/following-sibling::button[contains(@class,'dropDownMenu_arrowDow')]")
    CITY_KAZAN_OPTION = (By.XPATH, ".//input[@name='city']/parent::div/following-sibling::div/button/span[text()='Казань']")
    ARROW_CATEGORY = (By.XPATH, ".//input[@name='category']/following-sibling::button[contains(@class,'dropDownMenu_arrowDow')]")
    CATEGORY_BOOK_OPTION = (By.XPATH, ".//input[@name='category']/parent::div/following-sibling::div/button/span[text()='Книги']")
    TEXTAREA_DESCRIPTION = (By.XPATH, ".//textarea[@placeholder='Описание товара']")
    INPUT_PRICE = (By.NAME, "price")
    BUTTON_PUBLICATE = (By.XPATH, ".//button[text()='Опубликовать']")
