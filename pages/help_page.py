from symtable import Class
from time import sleep
from token import STRING

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


from pages.base_page import Page

class HelpPage(Page):
    # HEADER_RETURNS = (By.XPATH, "//h1[text() = ' Returns']")
    # HEADER_PROMOTION = (By.XPATH, "//h1[text() = ' Current promotions']")
    HEADER_TEXT = (By.XPATH, "//h1[text()=' {STRING}']")
    TOPIC_SELECTOR =(By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    #Dynamic Locator
    def _get_locator (self, expected_header_text):
        #(By.XPATH, "//h1[text() = ' Returns']")
        #(By.XPATH, "//h1[text() = ' Current promotions']")
        #(By.XPATH, "//h1[text() = ' {STRING}']") ==> (By.XPATH, "//h1[text() = ' Current promotions']")
        return [self.HEADER_TEXT[0], self.HEADER_TEXT[1].replace('{STRING}', expected_header_text)]


    def open_help_page(self):
        self.open('https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=')


    def select_topic(self,option):
        dd= self.find_element(*self.TOPIC_SELECTOR)
        select = Select(dd)
        select.select_by_value(option)
        sleep(3)

    def verify_header(self, expected_header_text):
        header_locator = self._get_locator(expected_header_text)
        self.wait_till_element_visiable(*header_locator)

    # def verify_return_open(self):
    #     self.verify_partial_text('Returns',*self.PAGE_TITLE)
    #
    # def verify_current_promotion(self):
    #     self.wait_till_element_visiable(*self.HEADER_PROMOTION)