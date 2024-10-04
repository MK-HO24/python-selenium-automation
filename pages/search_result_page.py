import selenium
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import Page




class SearchResultPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_result(self, product):
        self.verify_partial_text(product,*self.SEARCH_RESULT_HEADER)


        # actual_result = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        # assert product in actual_result, f'Expected {product}, got actual {actual_result}'

    def verify_product_in_url(self, product):
        self.verify_partial_url(product)
        # self.verify_partial_text(product, *self.SEARCH_RESULT_HEADER)