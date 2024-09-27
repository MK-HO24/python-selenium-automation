from itertools import product
from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main()



@when('Search for {product}')
def search_for_product(context, product):
    context.app.header.search_products(product)
    # context.driver.find_element(By.ID, 'search').send_keys(product)
    # context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()



@when('Click on cart icon')
def click_cart_icon(context):
    context.app.main_page.cart_icon()

    # context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()


@when('Click on Sign in icon')
def click_sign_in(context):
    context.app.main_page.signin_icon()



    # context.driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']//span[text()='Sign in']").click()






