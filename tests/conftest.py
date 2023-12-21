import pytest
from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from settings import config


@pytest.fixture()
def browser_management():
    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout
    if config.remote_url:
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=config.remote_url,
            options=options
        )

        browser_selenoid = Browser(Config(driver))
        yield browser_selenoid

        browser.quit()
    else:
        browser.config.driver_name = config.driver_name
        browser.config.window_height = config.window_height
        browser.config.window_width = config.window_width
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = config.load_strategy
        browser.config.driver_options = driver_options

        yield

        browser.quit()


@pytest.fixture()
def selenoid_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    browser.quit()
