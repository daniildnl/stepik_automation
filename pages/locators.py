from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a.btn')


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) strong')
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) strong')
    ALERT_SUCCESS_ADDED_TO_BASKET = (By.CSS_SELECTOR, '.alert-success')
