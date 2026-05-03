from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import _find_element


class text_in_element_is_not_empty(object):

    def __init__(self, locator, method):
        self.locator = locator
        self.method = method

    def __call__(self, driver):
        try:
            element_text = _find_element(driver, self.locator).text
            return self.method(element_text)
        except StaleElementReferenceException:
            return False
