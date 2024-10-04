from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from features.steps.target_app_ui_steps import click_pp_link
from pages.base_page import Page





class TargetAppPage(Page):
    PPLink = (By.XPATH,"//a[text()='Privacy policy']")

    def open_target_app(self):
        self.open('https://www.target.com/c/target-app/-/N-4th2r')


    def click_pp_link(self):
        self.wait_to_be_clickable_click(*self.PPLink)

    def verify_pp_open(self):
        self.verify_partial_url('target-privacy-policy')

    def close(self):
        self.driver.close()

