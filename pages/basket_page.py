from .base_page import BasePage
from .locators import BasketPageLocators
import time
import pytest


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "element is present"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_BUTTON), "basket is not empty"

