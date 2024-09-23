from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then
from time import sleep

@when('Add first search result to cart')
def add_first_search_result(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='chooseOptionsButton']").click()
    # sleep(5)
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class*='sc-529a2ea7-0 hbiLND']"))).click()

    # context.driver.find_element(By.CSS_SELECTOR,"div[class*='sc-529a2ea7-0 hbiLND']").click()

@when('Open target cart page')
def open_target_cart(context):
    context.driver.get('https://target.com/cart')


@then('Verify cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.empty_cart_check()
    # actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']//h1[text()='Your cart is empty']").text
    # expected_text = 'Your cart is empty'
    # assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'


@then('Verify cart is not empty')
def verify_cart_is_empty(context):
    # context.driver.find_element(By.XPATH,"//a[text()='View cart & check out']").click()
    actual_text = context.driver.find_element(By.XPATH,"//span[contains(@class,'sc-93ec7147-3 fUVkzh')]").text
    expected_text = '1 item'
    assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'


@then('Verify that correct result show {product}')
def verify_search_result(context, product):
    context.app.search_result_page.verify_search_result(product)
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # expected_result = product
    # assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'