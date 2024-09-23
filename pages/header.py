from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_products(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)


    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load