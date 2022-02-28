from pages.base_page import BasePage


class SearchPage(BasePage):
    title = {"id": "firstHeading"}

    def verify_title(self, title):
        return self.get_element_text(self.title) == title

