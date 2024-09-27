from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_TEXT = (By.XPATH, "//div[@data-test='boxEmptyMsg']//h1[text()='Your cart is empty']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div[class*='sc-529a2ea7-0 hbiLND']")
    CART_HEADER_TEXT = (By.XPATH, "//span[contains(@class,'sc-93ec7147-3 fUVkzh')]")

    def empty_cart_check (self):
       self.verify_text('Your cart is empty',*self.CART_TEXT)

       # actual_text = self.driver.find_element(*self.CART_TEXT).text
       # expected_text = 'Your cart is empty'
       # assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'

    def add_first_search_result (self):
        self.click(*self.ADD_TO_CART_BTN)
        self.wait_to_be_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)

        # context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
        # sleep(5)
        # context.driver.wait.until(
        # EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='sc-529a2ea7-0 hbiLND']"))).click()

    def verify_cart_is_not_empty(self):
        self.verify_partial_text('1 item',*self.CART_HEADER_TEXT)

    # actual_text = context.driver.find_element(By.XPATH, "//span[contains(@class,'sc-93ec7147-3 fUVkzh')]").text
    # expected_text = '1 item'
    # assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'