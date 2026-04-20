import allure
from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    TITLE_FORM = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    EMAIL_FIELD = (
        By.XPATH, ".//label[text()='Email']/following-sibling::input"
    )
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    def is_page_available(self):
        self.wait_element_clickable(ForgotPasswordPage.TITLE_FORM)
        return (
            self.driver.find_element(*ForgotPasswordPage.TITLE_FORM) and
            self.get_url() == data.FORGOT_PASSWORD_URL
        )

    @allure.step('Fill up email field {email}')
    def fill_email_up(self, email):
        self.wait_element_located(ForgotPasswordPage.EMAIL_FIELD)
        self.input(ForgotPasswordPage.EMAIL_FIELD, email)

    @allure.step('Press on button "Восстановление"')
    def restore_password(self):
        self.wait_element_clickable(ForgotPasswordPage.RESTORE_BUTTON)
        self.click(ForgotPasswordPage.RESTORE_BUTTON)
