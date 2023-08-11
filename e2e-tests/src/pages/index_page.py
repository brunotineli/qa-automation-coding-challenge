from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def page_title(self):
        self.driver.find_element(By.XPATH, '//h1[text()="Get Github Repos"]')

    def submit_search(self, search_term):
        self.driver.find_element(By.ID, 'username').send_keys(search_term)
        self.driver.find_element(By.CLASS_NAME, 'submit').click()

