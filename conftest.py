import pytest
from selenium import webdriver
import data


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(data.URL)
    firefox_driver.maximize_window()

    yield firefox_driver

    firefox_driver.quit()
