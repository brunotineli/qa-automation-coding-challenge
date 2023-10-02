from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

APP_URL = os.environ.get('APP_URL', 'http://localhost:3000/')
CLOUD_URL = os.environ.get('CLOUD_URL', 'http://localhost:4444')
IMPLICIT_WAIT_TIMEOUT = os.environ.get('IMPLICIT_WAIT_TIMEOUT', 15)
RUN_ON_CI = (os.environ.get("CI") is True)


def new_driver():
    options = FirefoxOptions()
    if RUN_ON_CI:
        driver = webdriver.Remote(command_executor=CLOUD_URL, options=options)
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
    driver.get(APP_URL)
    return driver
