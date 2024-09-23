from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_TEXT = (By.XPATH, "//div[@data-test='boxEmptyMsg']//h1[text()='Your cart is empty']")

    def empty_cart_check (self):
       actual_text = self.driver.find_element(*self.CART_TEXT).text
       expected_text = 'Your cart is empty'
       assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'

