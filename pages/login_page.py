from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")

    def go_to_forgot_password(self):
        self.click(LoginPage.FORGOT_PASSWORD_LINK)
