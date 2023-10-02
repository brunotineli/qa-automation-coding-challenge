from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from src.pages.base_page import BasePage


class IndexPage(BasePage):
    txt_search_element = (By.ID, 'username')
    txt_status_text = (By.CSS_SELECTOR, 'p.output-status-text')
    result_elements = (By.CSS_SELECTOR, 'li.repo-row')

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self):
        self.wait.until(ec.presence_of_element_located(self.txt_search_element))

    def clear_search(self):
        self.driver.find_element(*self.txt_search_element).clear()
        self.driver.find_element(*self.txt_search_element).send_keys(Keys.ENTER)
        self.wait.until(ec.presence_of_element_located(self.txt_status_text))

    def submit_search(self, search_term):
        self.driver.find_element(*self.txt_search_element).send_keys(search_term + Keys.ENTER)

    def search_results_list(self):
        results = []

        search_results = self.wait.until(ec.presence_of_all_elements_located(self.result_elements))
        for item in search_results:
            link_column = item.find_element(By.CSS_SELECTOR, 'a')
            description_column = item.find_element(By.CSS_SELECTOR, 'a')

            results.append(
                {
                    'title': link_column.text,
                    'link': link_column.get_attribute('href'),
                    'description': description_column.text
                }
            )

        return results

    def search_has_results(self):
        if len(self.search_results_list()) > 0:
            return True
        else:
            return False
