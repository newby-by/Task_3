import allure
from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


@allure.title('The page object for login page')
class LoginPage(BasePage):
    TITLE_PAGE = (By.XPATH, ".//h2[text()='Вход']")
    TITLE = 'Вход'
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    FIELD = lambda text: (
        By.XPATH, f".//label[text()='{text}']/following-sibling::input"
    )
    EMAIL = 'Email'
    PASSWORD = 'Пароль'
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    @allure.step('Click on forgot password link')
    def go_to_forgot_password(self):
        self.click(LoginPage.FORGOT_PASSWORD_LINK)

    @allure.step('Fill up email field with {email}')
    def fill_up_email_field(self, email):
        self.wait_element_located(LoginPage.FIELD(LoginPage.EMAIL))
        self.input(LoginPage.FIELD(LoginPage.EMAIL), email)

    @allure.step('Fill up password field with {password}')
    def fill_up_password_field(self, password):
        self.wait_element_located(LoginPage.FIELD(LoginPage.PASSWORD))
        self.input(LoginPage.FIELD(LoginPage.PASSWORD), password)

    @allure.step('Press the login button')
    def press_login(self):
        self.wait_element_clickable(LoginPage.LOGIN_BUTTON)
        self.click(LoginPage.LOGIN_BUTTON)

    @allure.step('Fill up login form')
    def fill_up_login_form(self, email, password):
        self.fill_up_email_field(email)
        self.fill_up_password_field(password)
        self.press_login()

    @allure.step('Check Login page is available')
    def is_page_available(self):
        self.wait_element_clickable(LoginPage.TITLE_PAGE)
        return (
            self.get_url() == data.LOGIN_URL and
            self.find_element(
                LoginPage.TITLE_PAGE).text == LoginPage.TITLE
        )
