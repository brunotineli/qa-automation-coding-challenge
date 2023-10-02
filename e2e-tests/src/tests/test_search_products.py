from src.conftest import new_driver
from src.pages.index_page import IndexPage


class TestSearchWithExistingGithubUsername:
    def setup_class(self):
        self.driver = new_driver()

        self.index_page = IndexPage(self.driver)
        self.index_page.is_page_loaded()

    def setup_method(self):
        self.index_page.clear_search()

    def teardown_class(self):
        self.driver.quit()

    def test_search_has_repos(self):
        self.index_page.submit_search('brunotineli')

        assert self.index_page.search_has_results()

    def test_search_and_go_to_first_found_repo(self):
        self.index_page.submit_search('brunotineli')

        # foo verification
        assert self.index_page.search_has_results()
