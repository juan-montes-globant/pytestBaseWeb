import os

from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import BASE_DIR_PATH


class DummyClass:
    file_path = BASE_DIR_PATH + '/'

    def login_facebook(self):
        driver = webdriver.Chrome(
            executable_path=self.file_path+'driver/chromedriver')
        driver.get("https://www.facebook.com")

        email_input = driver.find_element(By.ID, "email")
        email_input.click()
        email_input.send_keys("testmail@gmail.com")

        password_input = driver.find_element(By.ID, "pass")
        password_input.click()
        password_input.send_keys("testPassword123")

        log_in_button = driver.find_element(By.NAME, "login")
        log_in_button.click()

        driver.close()


def test_login():
    dummy_class = DummyClass()
    dummy_class.login_facebook()
