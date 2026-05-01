import allure
from selenium.webdriver.common.by import By

import pages


class OrdersPanelPage(pages.BasePage):
    # HISTORY = (
    #     By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]"
    # )
    ORDER_CARD = (
        By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]"
    )

    ORDERS_NUMBERS_IN_HISTORY = (
        By.XPATH, (".//li[contains(@class, 'OrderHistory_listItem')]"
                   "//p[contains(text(), '#')]")
    )

    @allure.step('Get ids orders')
    def get_orders_ids(self):
        self.wait_element_located(OrdersPanelPage.ORDERS_NUMBERS_IN_HISTORY)
        elements = self.find_elements(OrdersPanelPage.ORDERS_NUMBERS_IN_HISTORY)

        return OrdersPanelPage.get_text_from_elements(elements)

    @staticmethod
    def have_ids_in_orders_lists(*, ids_history, ids_orders_list):
        for id in ids_history:
            if id not in ids_orders_list:
                return False
        return True
