from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):

    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    SIGNIN_ICON = (By.XPATH,"//a[@data-test='@web/AccountLink']//span[text()='Sign in']")


    def open_main(self):
        self.open('https://www.target.com/')


    def cart_icon(self):
        self.wait_to_be_clickable_click(*self.CART_ICON)
        # self.click(*self.CART_ICON)
        sleep(6)

        # self.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

    def signin_icon(self):
        self.wait_to_be_clickable_click(*self.SIGNIN_ICON)



# main_page = MainPage()
# main_page.

