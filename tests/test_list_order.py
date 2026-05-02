import allure

import data
import pages


class TestListOrder:

    def test_click_order_open_modal_window(self, login_user_with_order):
        driver, id = login_user_with_order

        feed_page = pages.FeedPage(driver)
        feed_page.open(data.FEED_URL)

        feed_page.open_card_by_id(id)

        assert int(feed_page.get_id_order_in_window().split('#')[1]) == id

    @allure.title('Create an order')
    @allure.description('The order number is increased in all time '
                        'and today and id show up in In Progress')
    def test_create_order_data_in_list_change(self, login_user):
        nav_panel = pages.NavPanelPage(login_user)
        nav_panel.go_to_orders_list()

        feed_page = pages.FeedPage(nav_panel.driver)
        order_number_all_time_before = feed_page.get_orders_number_all_time()
        order_number_today_before = feed_page.get_orders_number_today()

        nav_panel = pages.NavPanelPage(feed_page.driver)
        nav_panel.go_to_constructor()

        main_page = pages.MainPage(nav_panel.driver)
        main_page.make_burger()
        main_page.click_on_order_button()
        id_order = main_page.get_order_number_in_window()

        main_page.close_window()

        nav_panel = pages.NavPanelPage(main_page.driver)
        nav_panel.go_to_orders_list()

        feed_page = pages.FeedPage(nav_panel.driver)
        order_number_all_time_after = feed_page.get_orders_number_all_time()
        order_number_today_after = feed_page.get_orders_number_today()
        id_order_in_progress = feed_page.get_id_order_in_progress()

        assert (
            int(order_number_all_time_after) >
            int(order_number_all_time_before)
            and
            int(order_number_today_after) > int(order_number_today_before)
            and
            int(id_order_in_progress) == int(id_order)
        ), (
            f"{id_order}:{id_order_in_progress}:"
            f"{order_number_all_time_before}:"
            f"{order_number_all_time_after}:{order_number_today_before}:"
            f"{order_number_today_after}"
        )

    def test_list_orders_and_history_orders(self, login_user_with_2_orders):
        nav_page = pages.NavPanelPage(login_user_with_2_orders)
        nav_page.go_to_account()
        account_page = pages.AccountPage(nav_page.driver)
        account_page.open_orders_history()

        orders_panel = pages.OrdersPanelPage(account_page.driver)
        orders_numbers_in_account = orders_panel.get_orders_ids()

        nav_page = pages.NavPanelPage(account_page.driver)
        nav_page.go_to_orders_list()

        orders_panel = pages.OrdersPanelPage(nav_page.driver)
        orders_numbers_in_orders_lists = orders_panel.get_orders_ids()

        assert pages.OrdersPanelPage.have_ids_in_orders_lists(
            ids_history=orders_numbers_in_account,
            ids_orders_list=orders_numbers_in_orders_lists
        )
