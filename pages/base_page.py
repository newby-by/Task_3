from abc import ABC

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable
)

from pages.expected_conditions import text_in_element_is_not_empty


class BasePage(ABC):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open the page with {url}")
    def open(self, url):
        self.driver.get(url)

    def wait_element_located(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            presence_of_element_located(locator)
        )
        return element

    def wait_element_clickable(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            element_to_be_clickable(locator)
        )
        self.scroll_to(locator)
        return element

    def wait_text_in_element(self, locator, method, time=10):
        element = WebDriverWait(self.driver, time).until(
            text_in_element_is_not_empty(locator, method)
        )
        return element

    @allure.step("Click on an element")
    def click(self, locator):
        element = self.wait_element_clickable(locator)
        self.scroll_to(locator)
        element.click()

    def get_attribute(self, locator, name):
        return self.wait_element_located(locator).get_attribute(name)

    def is_not_hidden(self, locator):
        return self.wait_element_located(locator).get_attribute('hidden')

    @allure.step("Scroll to an element")
    def scroll_to(self, locator):
        element = self.wait_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   element)

    def get_current_handle(self):
        return self.driver.current_window_handle

    def get_all_handles(self):
        return self.driver.window_handles

    @allure.step("Switch to window by handle {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def remove_cookie_window(self, locator):
        element = self.wait_element_located(locator)
        self.driver.execute_script("arguments[0].remove();", element)

    def get_url(self):
        return self.driver.current_url
