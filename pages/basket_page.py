from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Basket is not empty"

    def is_basket_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket have items"

