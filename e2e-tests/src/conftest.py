from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os


APP_URL = os.environ.get('APP_URL', 'http://localhost:3000/')
CLOUD_URL = os.environ.get('CLOUD_URL', 'http://localhost:4444')
IMPLICIT_WAIT_TIMEOUT = 15
WAIT_UNTIL_TIMEOUT = 15


def new_driver():
    options = FirefoxOptions()
    if os.environ.get("CI") == 'true':
        driver = webdriver.Remote(command_executor=CLOUD_URL, options=options)
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
    driver.get(APP_URL)
    return driver