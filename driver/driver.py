import os

from selenium import webdriver


class Driver:
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/'
    driver = None

    def __init__(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome(
                executable_path=self.file_path + 'chromedriver')
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver
