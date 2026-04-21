import allure

from pages.account_page import AccountPage
from pages.main_page import MainPage


@allure.feature('Tests for main page')
class TestMainPage:

    @allure.title('Available page of account for auth user')
    @allure.description('After click on link "Личный Кабинет" open account/profile page')
    def test_after_click_on_link_account_redirect_to_account_page(self, login):
        main_page = MainPage(login)
        main_page.go_to_account()
        
        account_page = AccountPage(main_page.driver)

        assert account_page.is_page_available()
