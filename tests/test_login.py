import pytest
from pages.login_page import LoginPage
from selenium import webdriver
from utilities.read_excel import get_login_data

@pytest.mark.parametrize('email,password', get_login_data())
def test_login(setup_and_teardown, email, password):
    lp = LoginPage(setup_and_teardown)
    lp.click_login_link()
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login_button()




'''def test_login2(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login_link()
    lp.enter_email('manoj@gmail.com')
    lp.enter_password('abc!123')
    lp.click_login_button()'''


'''def test_login2(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login_link()
    lp.enter_email('manoj1@gmail.com')
    lp.enter_password('1abc!123')
    lp.click_login_button()'''



