from selenium.webdriver.support.ui import WebDriverWait
from conftest import WAIT_UNTIL_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAIT_UNTIL_TIMEOUT)
