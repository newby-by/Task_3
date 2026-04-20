from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    TITLE_FORM = (By.XPATH, ".//h2[text()='Восстановление пароля']")

    def is_page_available(self):
        self.wait_element_clickable(ForgotPasswordPage.TITLE_FORM)
        return (
            self.driver.find_element(*ForgotPasswordPage.TITLE_FORM) and
            self.get_url() == data.FORGOT_PASSWORD_URL
        )
