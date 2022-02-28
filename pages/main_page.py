from pages.base_page import BasePage


class MainPage(BasePage):
    container = {"id": "mw-content-text"}

    def verify_language(self, language:str):
        language = language.lower()[0:2]
        language_ele = self.get_element(self.container)
        return language_ele.get_attribute("lang") == language
