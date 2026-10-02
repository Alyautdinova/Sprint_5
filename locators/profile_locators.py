from selenium.webdriver.common.by import By

class ProfileLocators:
    LISTNING_NAME = (By.XPATH, ".//div[@class='card']//div[@class='about']/h2")
    LISTNING_CITY = (By.XPATH, ".//div[@class='card']//div[@class='about']/h3")
    LISTNING_PRICE = (By.XPATH, ".//div[@class='card']//div[@class='price']/h2")
