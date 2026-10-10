from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    login_link = (By.XPATH, '//a[text()="Log in"]')
    email = (By.ID, 'Email')
    password = (By.ID, 'Password')
    login_button = (By.XPATH, '//input[@value="Log in"]')

    def click_login_button(self):
        self.click(self.login_button)

    def click_login_link(self):
        self.click(self.login_link)

    def enter_email(self,email_value):
        self.send_keys(self.email,email_value)

    def enter_password(self,password_value):
        self.send_keys(self.password,password_value)