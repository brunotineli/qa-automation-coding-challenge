from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class IndexPage(BasePage):
    page_title_element = (By.XPATH, '//h1[text()="Get Github Repos"]')
    search_input_element = (By.ID, 'username')
    result_items_links = (By.XPATH, '//li[@class="repo-row"]/p/a')

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self):
        self.wait.until(
            ec.visibility_of_element_located(self.page_title_element)
        )

    def submit_search(self, search_term):
        self.wait.until(
            ec.presence_of_element_located(self.search_input_element)
        ).send_keys(search_term + Keys.ENTER)

    def is_search_with_repos(self):
        try:
            self.wait.until(
                ec.presence_of_all_elements_located(self.result_items_links)
            )
            return True
        except Exception:
            return False
