from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR,"#product_description")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alertinner>strong")
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR,".product_main h1")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    PRICE_IN_DESCRIPTION = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,"div.product_main p.price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span .btn[href*=basket]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")



class BasketPageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "h2.h3")
    # для проверки негативного сценария
    # ITEM_IN_BASKET = (By.CSS_SELECTOR, "#login_link")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "#content_inner a")