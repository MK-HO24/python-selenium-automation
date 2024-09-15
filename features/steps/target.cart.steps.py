from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Add first search result to cart')
def add_first_search_result(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='chooseOptionsButton']").click()
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,"div[class*='sc-529a2ea7-0 hbiLND']").click()



@then('Verify cart is not empty')
def verify_cart_is_empty(context):
    context.driver.find_element(By.XPATH,"//a[text()='View cart & check out']").click()
    actual_text = context.driver.find_element(By.XPATH,"//span[contains(@class,'sc-93ec7147-3 fUVkzh')]").text
    expected_text = '1 item'
    assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'

