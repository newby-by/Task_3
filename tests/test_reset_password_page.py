import allure

import data


@allure.feature('Tests for Reset Password page')
class TestResetPasswordPage:

    @allure.title('Form Reset password')
    @allure.description('Show password after click visibility button')
    def test_after_fill_up_form_and_click_button_redirect_to_reset_password_page(self, reset_password_page):
        reset_password_page.show_password()

        assert reset_password_page.is_password_visible()
