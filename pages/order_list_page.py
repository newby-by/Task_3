import allure
from selenium.webdriver.common.by import By

import data
import pages


class FeedPage(pages.BasePage):
    TITLE_PAGE = (By.XPATH, ".//h1")
    TITLE = 'Лента заказов'

    @allure.step('Check Feed page is available')
    def is_page_available(self):
        self.wait_element_clickable(FeedPage.TITLE_PAGE)
        return (
            self.get_url() == data.FEED_URL and
            self.find_element(FeedPage.TITLE_PAGE).text == FeedPage.TITLE
        )
