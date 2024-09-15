from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://target.com/')


@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(15)


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()
    sleep(8)

@when('Click on Sign in icon')
def click_sign_in(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']//span[text()='Sign in']").click()
    sleep(3)


@when('Click Sign in Right Nav Menu')
def click_sign_in_right(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()
    sleep(4)

@then('Verify that correct result show {product}')
def verify_search_result(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    expected_result = product
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'


@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']//h1[text()='Your cart is empty']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'

@then ('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'