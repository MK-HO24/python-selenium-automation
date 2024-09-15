from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

sleep(8)
#driver.find_element(By.CSS_SELECTOR, )

#by CSS, By id

driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")

#by CSS, By Class
driver.find_element(By.CSS_SELECTOR,".nav-input.nav-progressive-attribute")

#By CSS, By Tag and ID
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox")

#By CSS, all together
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox.nav-input.nav-progressive-attribute")

driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox.nav-input.nav-progressive-attribute[name='field-keywords'][tabindex='0']")

#attribute that contains partial values

driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox[name*='field-keyw'][tabindex='0']")

#By CSS By ID By Class
#driver.find_element(By.CSS_SELECTOR,"#continue.a-button-primary")

#By CSS from parent to child (separated by space)
#driver.find_element(By.CSS_SELECTOR, ".a-section .a-section #legalTextRow")