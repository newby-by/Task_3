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
        f".//ul[contains(@class, 'OrderFeed_list')]//p[contains(text(),'{id}')]"
    )
    ORDER_CARD_LINK = lambda id: (
        By.XPATH,
        (".//ul[contains(@class, 'OrderFeed_list')]"
         f"//p[contains(text(),'{id}')]/parent::div/parent::a")
    )
    ORDER_ID_IN_WINDOW = (
        By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p"
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

    @allure.step('Open an order card by id')
    def get_id_order_in_window(self):
        return self.find_element(FeedPage.ORDER_ID_IN_WINDOW).text
