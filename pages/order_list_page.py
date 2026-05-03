import allure
from selenium.webdriver.common.by import By

import data
import pages


class FeedPage(pages.BasePage):
    TITLE_PAGE = (By.XPATH, ".//h1")
    TITLE = 'Лента заказов'
    ORDER_CARD_BY_NUMBER = lambda number: (
        By.XPATH, f"(.//ul[contains(@class, 'OrderFeed_list')]/li)[{number}]"
    )
    ORDER_CARD_BY_ID = lambda id: (
        By.XPATH,
        (".//ul[contains(@class, 'OrderFeed_list')]"
         f"//p[contains(text(),'{id}')]")
    )
    ORDER_CARD_LINK = lambda id: (
        By.XPATH,
        (".//ul[contains(@class, 'OrderFeed_list')]"
         f"//p[contains(text(),'{id}')]/parent::div/parent::a")
    )
    ORDER_ID_IN_WINDOW = (
        By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p"
    )

    ORDER_IN_PROGRESS = (
        By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')]/li"
    )
    ORDERS_NUMBER_ALL_TIME = (
        By.XPATH,
        ".//p[text()='Выполнено за все время:']/following-sibling::p"
    )
    ORDERS_NUMBER_TODAY = (
        By.XPATH,
        ".//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )

    @allure.step('Check Feed page is available')
    def is_page_available(self):
        self.wait_element_clickable(FeedPage.TITLE_PAGE)
        return (
            self.get_url() == data.FEED_URL and
            self.find_element(FeedPage.TITLE_PAGE).text == FeedPage.TITLE
        )

    @allure.step('Open an order card by id {id}')
    def open_card_by_id(self, id):
        self.click(FeedPage.ORDER_CARD_LINK(id))

    def get_id_order_in_window(self):
        return self.find_element(FeedPage.ORDER_ID_IN_WINDOW).text

    def get_id_order_in_progress(self):
        self.wait_visibility_of_element_located(FeedPage.ORDER_IN_PROGRESS)
        self.wait_text_in_element_disappeared(
            FeedPage.ORDER_IN_PROGRESS, 'Все текущие заказы готовы!'
        )
        return self.find_element(FeedPage.ORDER_IN_PROGRESS).text

    def get_orders_number_all_time(self):
        return self.find_element(FeedPage.ORDERS_NUMBER_ALL_TIME).text

    def get_orders_number_today(self):
        return self.find_element(FeedPage.ORDERS_NUMBER_TODAY).text
