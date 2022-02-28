from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.search_page import SearchPage


class HomePage(BasePage):
    title = {"class_name": "central-textlogo__image"}
    search_field = {"id": "searchInput"}
    search_button = {"class_name": "pure-button"}
    languages = {"css": ".link-box Strong"}

    def verify_wikipedia_title(self):
        return self.get_element_text(self.title) == "Wikipedia"

    def search_word(self, word):
        self.send_text(self.search_field, word)
        self.click_element(self.search_button)
        return SearchPage(self.driver)

    def select_language(self, language):
        ele_languages = self.get_elements(self.languages)
        ele_language = list(filter(lambda element: element.text == language,
                                   ele_languages))
        [element.click() for element in ele_language]
        return MainPage(self.driver)
