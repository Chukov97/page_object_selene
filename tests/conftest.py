import pytest
from selene import browser
from selenium import webdriver
from settings import config
from utils import attach


@pytest.fixture()
def browser_management():
    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout
    browser.config.window_height = config.window_height
    browser.config.window_width = config.window_width
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = config.load_strategy
    browser.config.driver_options = driver_options

    if config.remote_url:
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        driver_options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=config.remote_url,
            options=driver_options
        )

        browser.config.driver = driver

    else:
        browser.config.driver_name = config.driver_name

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
