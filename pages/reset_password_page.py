import allure
from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    ACTIVE_FIELD_CLASS = 'input_status_active'
    PASSWORD_FIELD = (
        By.XPATH, ".//label[text()='Пароль']/following-sibling::input"
    )
    PIN_LABEL_FIELD = (By.XPATH, ".//label[text()='Введите код из письма']")
    SHOW_PASSWORD_BUTTON = (
        By.XPATH, ".//div[contains(@class, 'input__icon')]"
    )

    @allure.step('Click on visibility password icon')
    def show_password(self):
        self.wait_element_clickable(ResetPasswordPage.SHOW_PASSWORD_BUTTON)
        self.click(ResetPasswordPage.SHOW_PASSWORD_BUTTON)

    @allure.step('Fill up password field {password}')
    def fill_password_up(self, password):
        self.wait_element_located(ResetPasswordPage.PASSWORD_FIELD)
        self.input(ResetPasswordPage.PASSWORD_FIELD, password)

    def is_page_available(self):
        self.wait_element_clickable(ResetPasswordPage.PIN_LABEL_FIELD)
        return (
            self.driver.find_element(*ResetPasswordPage.PIN_LABEL_FIELD) and
            self.get_url() == data.RESET_PASSWORD_URL
        )

    def is_password_visible(self):
        self.wait_element_located(ResetPasswordPage.PASSWORD_FIELD)
        return self.get_attribute(ResetPasswordPage.PASSWORD_FIELD,
                                  'type') == 'text'

    def is_active_field_password(self):
        self.wait_element_located(ResetPasswordPage.PASSWORD_FIELD)
        return (ResetPasswordPage.ACTIVE_FIELD_CLASS in
                self.get_attribute(ResetPasswordPage.PASSWORD_FIELD, 'class'))
