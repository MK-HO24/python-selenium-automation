from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):

    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")


    def open_main(self):
        self.open('https://www.target.com/')


    def cart_icon(self):
        self.click(*self.CART_ICON)
        sleep(6)

        # self.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()





# main_page = MainPage()
# main_page.

