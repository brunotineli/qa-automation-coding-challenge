from conftest import new_driver
from pages.index_page import IndexPage

class TestSearchWithExistingGithubUsername:
    def setup_method(self, method):
        self.driver = new_driver()
        self.index_page = IndexPage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test_pass(self):
        self.index_page.page_title()
