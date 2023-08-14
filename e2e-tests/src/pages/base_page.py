from selenium.webdriver.support.ui import WebDriverWait
import os

WAIT_UNTIL_TIMEOUT = os.environ.get('WAIT_UNTIL_TIMEOUT', 15)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAIT_UNTIL_TIMEOUT)
