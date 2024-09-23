from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart_page = CartPage(driver)
