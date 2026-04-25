from ast import main
import random

import allure

import data
import pages
from pages.main_page import MainPage


@allure.feature('Tests for main page (constructor page)')
class TestMainPage:

    @allure.title('Available page of account for auth user')
    @allure.description('After click on link '
                        '"Личный Кабинет" open account/profile page')
    def test_after_click_on_link_account_redirect_to_account_page(
        self, login_user
    ):
        nav_page = pages.NavPanelPage(login_user)
        nav_page.go_to_account()    
        account_page = pages.AccountPage(nav_page.driver)

        assert account_page.is_page_available()

    @allure.title('An ingredient card')
    @allure.description('After click on a card with name'
                        'modal window has the title and name is the same')
    def test_click_on_ingredient_open_window_with_expected_data(
        self, login_user
    ):
        main_page = pages.MainPage(login_user)
        random_card_number = random.randint(1, main_page.number_of_cards)
        expected_data = main_page.get_ingredient_data_from_constructor(
            random_card_number
        )
        main_page.open_ingredient_card_with(random_card_number)

        assert (
            main_page.get_title_ingredient_modal_window() ==
            MainPage.TITLE_MODAL_WINDOW
            and
            main_page.get_name_ingredient_modal_window() ==
            expected_data.get('name') 
        )

    @allure.title('An ingredient card')
    @allure.description('The cross button for closing a card')
    def test_click_on_cross_ingredient_window_closed(self, login_user):
        main_page = pages.MainPage(login_user)
        random_card_number = random.randint(1, main_page.number_of_cards)
        main_page.open_ingredient_card_with(random_card_number)

        main_page.close_ingredient_card()

        assert (
            main_page.find_element(MainPage.TITLE_PAGE).text ==
            MainPage.TITLE
        )

    @allure.title('Drag and drop an ingredient to constructor')
    @allure.description('The counter of an ingredient is changed')
    def test_drag_and_drop_ingredient_counter_changed(self, login_user):
        main_page = pages.MainPage(login_user)
        random_card_number = random.randint(1, main_page.number_of_cards)
        card_data_before = main_page.get_ingredient_data_from_constructor(
            random_card_number
        )

        main_page.drag_and_drop_card_to_constructor_with(random_card_number)

        card_data_after = main_page.get_ingredient_data_from_constructor(
            random_card_number
        )

        assert (int(card_data_after.get('counter')) ==
                int(card_data_before.get('counter')) + 1) 
    
    @allure.title('Create an order')
    @allure.description('By an auth user it is possible')
    def test_auth_user_can_order(self, login_user):
        main_page = pages.MainPage(login_user)

        random_card_number = random.randint(1, main_page.number_of_cards)
        main_page.drag_and_drop_card_to_constructor_with(random_card_number)
        main_page.click_on_order_button()

        assert main_page.is_order_window_available()
