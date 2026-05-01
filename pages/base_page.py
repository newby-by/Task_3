from abc import ABC
from typing import List

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable,
    presence_of_element_located,
    visibility_of_element_located,
    text_to_be_present_in_element,
)
from seletools.actions import drag_and_drop as _drag_and_drop

from pages.expected_conditions import text_in_element_is_not_empty


class BasePage(ABC):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open the page with {url}")
    def open(self, url):
        self.driver.get(url)

    def wait_element_located(self, locator, timeout=10):
        WebDriverWait(
            driver=self.driver,
            timeout=timeout).until(
            presence_of_element_located(locator)
        )
    
    def wait_text_in_element_disappeared(self, locator, text_, timeout=10):
        WebDriverWait(
            driver=self.driver,
            timeout=timeout).until_not(
            text_to_be_present_in_element(locator, text_)
        )
    
    def wait_element_disappeared(self, locator, timeout=10):
        WebDriverWait(
            driver=self.driver,
            timeout=timeout).until_not(
            presence_of_element_located(locator)
        )
     
    def wait_visibility_of_element_located(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            visibility_of_element_located(locator)
        )

    def wait_element_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            element_to_be_clickable(locator)
        )
        self.scroll_to(locator)

    def wait_text_in_element(self, locator, method, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            text_in_element_is_not_empty(locator, method)
        )

    @allure.step("Click on an element")
    def click(self, locator):
        self.wait_element_located(locator)
        self.wait_visibility_of_element_located(locator)
        self.wait_element_clickable(locator)
        self.scroll_to(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Input text")
    def input(self, locator, text):
        self.wait_element_located(locator)
        self.driver.find_element(*locator).send_keys(text)

    def get_attribute(self, locator, name):
        self.wait_element_located(locator)
        return self.driver.find_element(*locator).get_attribute(name)

    def is_not_hidden(self, locator):
        self.wait_element_located(locator)
        return self.driver.find_element(*locator).get_attribute('hidden')

    @allure.step("Scroll to an element")
    def scroll_to(self, locator):
        self.wait_element_located(locator)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   element)

    def get_current_handle(self):
        return self.driver.current_window_handle

    def get_all_handles(self):
        return self.driver.window_handles

    @allure.step("Switch to window by handle {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def remove_element_from_dom(self, locator):
        try:
            self.wait_element_located(locator, 2)
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].remove();", element)
        except TimeoutException:
            ...

    def get_url(self):
        return self.driver.current_url
    
    def find_element(self, locator):
        self.wait_element_located(locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.wait_element_located(locator)
        return self.driver.find_elements(*locator)

    @allure.step("Drag and drop {source_element} to {target_element}")
    def drag_and_drop(self, source_element, target_element):
        _drag_and_drop(self.driver, source_element, target_element)

    @staticmethod
    def get_text_from_elements(elements: List[WebElement]) -> List[str]:
        return [el.text for el in elements]
