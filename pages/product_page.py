from .base_page import BasePage
from .locators import ProductPageLocators

book_name = "Coders at Work"
book_price = "£19.99"


class ProductPage(BasePage):

    # говорит о том, что это страница товара. Так как на других страницах нет описания товара
    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION)

    # говорит о том, что на странице есть кнопка добавления в корзину
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "add to basket button is not present"

    # после добавления книги в корзину пояляется окно с информацией о добавлении товара в корзину
    def should_be_success_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), "item wasn't added"

    def should_be_appropriate_name_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET) == self.browser.find_element(*ProductPageLocators.BOOK_NAME).text(), "not the same book"

    def should_be_appropriate_price_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_IN_DESCRIPTION) == self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET), "not the same price"

    def get_the_product_name(self):
        # print(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text)
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)

    def get_the_product_price(self):
        # print(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == book_price, "price is incorrect"

    def should_be_correct_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == book_name, "product name is incorrect"

    def should_be_correct_product_name_in_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_ALERT).text, "wrong product name in alert"

    def should_be_correct_product_price_in_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRICE_IN_ALERT).text, "wrong product price in alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Success message still in there"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
