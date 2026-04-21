import allure
import pytest

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature('Tests for account page')
class TestAccountPage:

    @allure.title('The history is available for auth user')
    @allure.description('Check UL element in DOM. '
                        'User could has orders or not.')
    @pytest.mark.parametrize(
        'fixture',
         ['login_user', 'login_user_with_2_orders']
    )
    def test_auth_user_can_see_order_history_in_account_page(
        self, fixture, request
    ):
        driver = request.getfixturevalue(fixture)
        main_page = MainPage(driver)
        main_page.go_to_account()

        account_page = AccountPage(main_page.driver)
        account_page.open_orders_history()

        assert account_page.is_history_available()
    
    @allure.title('The exit button is available for auth user')
    @allure.description('After press exit button redirect to login page.')
    def test_auth_user_after_press_exit_button_redirect_to_login_page(self, login_user):
        main_page = MainPage(login_user)
        main_page.go_to_account()

        account_page = AccountPage(main_page.driver)
        account_page.press_exit()

        login_page = LoginPage(account_page.driver)

        assert login_page.is_page_available()
