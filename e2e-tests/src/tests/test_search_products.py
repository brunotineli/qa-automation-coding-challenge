from conftest import new_driver
from pages.index_page import IndexPage

class TestSearchWithExistingGithubUsername:
    def setup_method(self, method):
        self.driver = new_driver()

        self.index_page = IndexPage(self.driver)
        self.index_page.is_page_loaded()


    def teardown_method(self, method):
        self.driver.quit()

    def test_search_and_go_to_first_found_repo(self):
        self.index_page.submit_search('brunotineli')

        # foo verification
        assert self.index_page.is_search_with_repos()