from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait



class BasePage:
    def __init__(self, driver):
        self.driver:webdriver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_locator(self, locator_info):
        locator_type = None
        locator_value = None
        for key, value in locator_info.items():
            locator_type = self.get_by_type(key)
            locator_value = value
        return locator_type, locator_value

    @staticmethod
    def get_by_type(locator_type):
        locator = {"id": By.ID,
                   "name": By.NAME,
                   "class_name": By.CLASS_NAME,
                   "link_text": By.LINK_TEXT,
                   "tag_name": By.TAG_NAME,
                   "partial_link_text": By.PARTIAL_LINK_TEXT,
                   "css": By.CSS_SELECTOR,
                   "xpath": By.XPATH
                   }

        if locator_type not in locator:
            self.log.write_message_error("Locator type exception occurred- " + log_info,
                                         self.driver.current_url, start_time)
            raise AttributeError
        return locator[locator_type]

    def get_element(self, locator_info):
        locator_type, locator_value = self.get_locator(locator_info)
        return self.wait.until(expected_conditions.presence_of_element_located(
            (locator_type, locator_value)))

    def get_elements(self, locator_info):
        locator_type, locator_value = self.get_locator(locator_info)
        return self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (locator_type, locator_value)))

    def wait_element_clickable(self, locator_info):
        locator_type, locator_value = self.get_locator(locator_info)
        return self.wait.until(expected_conditions.element_to_be_clickable(
            (locator_type, locator_value)))

    def click_element(self, locator_info):
        element = self.wait_element_clickable(locator_info)
        element.click()

    def send_text(self, locator_info, text):
        element = self.get_element(locator_info)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator_info):
        return self.get_element(locator_info).text