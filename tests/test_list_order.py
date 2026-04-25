import data
import pages


class TestList_Order:

    def test_click_order_open_modal_window(self, login_user_with_order):
        driver, id = login_user_with_order

        feed_page = pages.FeedPage(driver)
        feed_page.open(data.FEED_URL)

        feed_page.open_card_by_id(id)
        
        assert int(feed_page.get_id_order_in_window().split('#')[1]) == id
