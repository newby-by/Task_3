import allure

import pages


@allure.feature('Tests for main page (constructor page)')
class TestMainPage:

    @allure.title('Available page of account for auth user')
    @allure.description('After click on link "Личный Кабинет" open account/profile page')
    def test_after_click_on_link_account_redirect_to_account_page(self, login_user):
        nav_page = pages.NavPanelPage(login_user)
        nav_page.go_to_account()    
        account_page = pages.AccountPage(nav_page.driver)

        assert account_page.is_page_available()
