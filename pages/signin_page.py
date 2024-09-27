from importlib.metadata import pass_none
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class SigninPage(Page):
    ACCOUNT_NAV_SIGNIN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")
    SIGNIN_PAGE_HEADER = (By.XPATH,"//span[text()='Sign into your Target account']")
    USERNAME_FIELD = (By.ID,"username")
    PASSWORD_FIELD = (By.ID,"password")
    SIGNIN_BTN = (By.ID, "login")

    def click_sign_in_right(self):
        self.wait_to_be_clickable_click(*self.ACCOUNT_NAV_SIGNIN)



    def verify_sign_in_form(self):
        self.verify_text("Sign into your Target account", *self.SIGNIN_PAGE_HEADER)


    def input_user_name(self):
        self.input_text("epederson@marattok.com",*self.USERNAME_FIELD)


    def input_password(self):
        self.input_text("F*******",*self.PASSWORD_FIELD)




    def click_signin_button(self):
        self.click(*self.SIGNIN_BTN)

    def verify_user_is_logged_in(self):
        self.wait_for_element_to_disappear(*self.SIGNIN_BTN)