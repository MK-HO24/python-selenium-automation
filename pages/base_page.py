from urllib3.util import url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open(self,url):
        self.driver.get(url)


    def find_element(self,*locator):
        return self.driver.find_element(*locator)


    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)


    def get_text(self, *locator):
        return self.driver.find_element(*locator).text


    def click(self,*locator):
        self.find_element(*locator).click()


    def input_text(self,text,*locator):
        self.find_element(*locator).send_keys(text)


    def wait_to_be_clickable(self,*locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} is not clickable"
        )


    def wait_to_be_clickable_click(self,*locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} is not clickable"
        ).click()


    def wait_till_element_visiable(self,*locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element by {locator} is not visiable"
        )


    def wait_for_element_to_disappear(self,*locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"Element by {locator} is still visiable"
        )


    def verify_text(self,expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text}, got actual {actual_text}'


    def verify_partial_text(self,expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not found in actual {actual_text}'


    def verify_product_url(self,expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got actual {actual_text}'


    def verify_product_partial_url(self,expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected {expected_url} not found in actual {actual_text}'