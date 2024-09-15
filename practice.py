from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from target_search import expected_result

#from target_search import actual_result, expected_result

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
# driver.find_element(By.ID,'twotabsearchtextbox').send_keys('socks')
# driver.find_element(By.ID,'nav-search-submit-button').click()

#driver.find_element(By.XPATH,"//img[@alt='Shop Studio Pro headphones']")
#driver.find_element(By.XPATH,"//input[@name='field-keywords']").send_keys('socks')
#driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon']").send_keys('shirt')
#driver.find_element(By.ID,'nav-search-submit-button').click()
#driver.find_element(By.XPATH,"//a[@class='nav-a  ']" and "//a[@tabindex='0']" and "//a[@data-csa-c-slot-id='nav_cs_2']").click()
#driver.find_element(By.XPATH,"//a[text()= 'Best Sellers' and @class = 'nav-a  ']").click()
#driver.find_element(By.XPATH, "//*[@name='field-keywords']")
#driver.find_element(By.XPATH,"//*[text()= 'Best Sellers' and @class = 'nav-a  ']").click()
#driver.find_element(By.XPATH,"//div[@id='nav-main']//a[@tabindex = '0' and text() = 'Best Sellers']").click()

# driver.find_element(By.ID,'search').send_keys('tea')
# driver.find_element(By.XPATH,"//button[@aria-label='search']").click()
#
# sleep(4)
#
# actual_result = driver.find_element(By.XPATH,"//div[@data-test='results-facets-row']").text
# expected_result = 'tea00'
#
# assert expected_result in actual_result,f"Expected {expected_result}, but got {actual_result}"
# print("Test case passed")
#
# driver.quit()

sleep(2)

driver.find_element(By.ID,'search').send_keys('tea')
driver.find_element(By.XPATH,'//button[@data-test="@web/Search/SearchButton"]').click()

actual_result= driver.find_element(By.XPATH,"//div[@data_test='resultsHeading']").txet
expected_result = "tea"

if actual_result==expected_result:
    print("Test passed")
sleep(15)