from pages.home_page import HomePage


class TestSuite:

    def test_search(self, setup):
        home_page = HomePage(setup)
        assert home_page.verify_wikipedia_title()
        search_page = home_page.search_word("Python")
        assert search_page.verify_title("Python")

    def test_language(self,setup):
        home_page = HomePage(setup)
        assert home_page.verify_wikipedia_title()
        main_page = home_page.select_language("English")
        assert main_page.verify_language("English")
