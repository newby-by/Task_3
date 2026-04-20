import allure

import data
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature('Tests for Forgot Password page')
class TestForgotPasswordPage:

    @allure.title('Form Восстановление пароля')
    @allure.description('After input an email and press button '
                        '"Восстановить" move to reset password page')
    def test_after_fill_up_form_and_click_button_redirect_to_reset_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open(data.FORGOT_PASSWORD_URL)
        forgot_password_page.fill_email_up(data.UserData().email)
        forgot_password_page.restore_password()

        reset_password_page = ResetPasswordPage(forgot_password_page.driver)

        assert reset_password_page.is_page_available()
