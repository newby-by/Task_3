import allure

import data
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.feature('Tests for Login page')
class TestLoginPage:

    @allure.title('Can move from login page to forgot password page')
    @allure.description('By link "Восстановление пароля"')
    def test_move_from_login_page_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open(data.LOGIN_URL)
        login_page.go_to_forgot_password()

        forgot_password_page = ForgotPasswordPage(login_page.driver)

        assert forgot_password_page.is_page_available()
