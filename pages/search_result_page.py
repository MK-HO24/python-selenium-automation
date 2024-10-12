import selenium
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#import select to used with "Select" dropdown menu
from pages.base_page import Page



class SearchResultPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    FAV_ICON = (By.XPATH, "//button[@data-test='FavoritesButton']")
    FAV_TOOLTIP = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")


    def verify_search_result(self, product):
        self.verify_partial_text(product,*self.SEARCH_RESULT_HEADER)


        # actual_result = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        # assert product in actual_result, f'Expected {product}, got actual {actual_result}'

    def verify_product_in_url(self, product):
        self.verify_partial_url(product)
        # self.verify_partial_text(product, *self.SEARCH_RESULT_HEADER)


    def hover_favorite(self):
        heart_icon = self.find_element(*self.FAV_ICON)

        actions = ActionChains(self.driver)
        actions.move_to_element(heart_icon)
        actions.perform()


    def verify_favorite(self):
        self.wait_till_element_visiable(*self.FAV_TOOLTIP)

