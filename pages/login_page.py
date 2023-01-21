from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "not login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form isn't present"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_input.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()
