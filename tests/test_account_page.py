import allure
import pytest

from pages.account_page import AccountPage
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
