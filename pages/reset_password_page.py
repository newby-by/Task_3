from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    PIN_LABEL_FIELD = (By.XPATH, ".//label[text()='Введите код из письма']")

    def is_page_available(self):
        self.wait_element_clickable(ResetPasswordPage.PIN_LABEL_FIELD)
        return (
            self.driver.find_element(*ResetPasswordPage.PIN_LABEL_FIELD) and
            self.get_url() == data.RESET_PASSWORD_URL
        )
