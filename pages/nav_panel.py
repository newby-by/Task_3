import allure
from selenium.webdriver.common.by import By

from pages import BasePage


class NavPanelPage(BasePage):
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    ORDER_LIST_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    OVERLAY = lambda num: (By.XPATH, f"(.//div[contains(@class, 'Modal_modal_overlay')])[{num}]")
    
    @allure.step('Move to Constructor page')
    def go_to_constructor(self):
        self.click(NavPanelPage.CONSTRUCTOR_LINK)

    @allure.step('Move to Order page')
    def go_to_orders_list(self):
        self.remove_element_from_dom(NavPanelPage.OVERLAY(2))        
        self.click(NavPanelPage.ORDER_LIST_LINK)

    @allure.step('Move to Account page')
    def go_to_account(self):
        self.remove_element_from_dom(NavPanelPage.OVERLAY(2))
        self.scroll_to(NavPanelPage.ACCOUNT_LINK)
        self.click(NavPanelPage.ACCOUNT_LINK)
