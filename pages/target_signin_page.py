from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from features.steps.target_app_ui_steps import click_pp_link
from pages.base_page import Page


class TargetSigninPage(Page):
    SIGNIN_ICON = (By.XPATH,"//span[text()='Sign in']")
    SIDE_NAV_ICON = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")
    TCLINK = (By.XPATH, "//a[text() = 'Target terms and conditions']")

    def open_signin_page(self):
        self.open('https://www.target.com')
        self.wait_to_be_clickable_click(*self.SIGNIN_ICON)
        self.wait_to_be_clickable_click(*self.SIDE_NAV_ICON)


    def click_on_tc_link(self):
        self.wait_to_be_clickable_click(*self.TCLINK)


    def verify_tc_open(self):
        self.verify_partial_url('terms-conditions')


    def close(self):
        self.driver.close()




