import pytest
from selene import browser
from selenium import webdriver
from demoqa_tests.models.constatn import BASE_URL


@pytest.fixture()
def browser_management():
    browser.config.base_url = BASE_URL
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()
