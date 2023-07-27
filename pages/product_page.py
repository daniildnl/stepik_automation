from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_btn()
        add_to_basket_btn = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), 'Add to basket button is not presented'

    def should_be_same_name_in_alert(self):
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.driver.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name == alert_product_name, \
            f"Product name in alert is not equal to the product name {alert_product_name} != {product_name}"

    def should_be_same_price_in_alert(self):
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_product_price = self.driver.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert product_price == alert_product_price, \
            f"Product price in alert is not equal to the product price {alert_product_price} != {product_price}"

    def success_alert_isnt_present(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_ADDED_TO_BASKET), 'Success alert is presented'

    def success_alert_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS_ADDED_TO_BASKET), 'Success alert doesnt disappeared'