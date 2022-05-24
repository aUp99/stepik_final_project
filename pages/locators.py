from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")