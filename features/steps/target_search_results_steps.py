from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then
from time import sleep



@then('Verify that correct result show {product}')
def verify_search_result(context, product):
    context.app.search_result_page.verify_search_result(product)
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # expected_result = product
    # assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'


@then('Verify that product {product} in URL')
def verify_product_url(context, product):
    context.app.search_result_page.verify_product_in_url(product)


@when('Hover favorite icon')
def hover_favorite(context):
    context.app.search_result_page.hover_favorite()


@then('favorite tool tip is shown')
def verify_favorite(context):
    context.app.search_result_page.verify_favorite()
