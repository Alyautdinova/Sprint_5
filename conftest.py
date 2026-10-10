import pytest
from selenium import webdriver

@pytest.fixture
def googleDriver():
    chrome_options = webdriver.ChromeOptions() # создали объект для опций
    driver = webdriver.Chrome(options=chrome_options) # создали драйвер и передали в него настройки

    yield driver

    driver.quit()
