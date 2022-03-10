from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from time import sleep

path_driver = '/home/dopel/codeInTest/tmp_testing/Wed-2022-03-09/geckodriver'

driver = webdriver.Firefox(executable_path=path_driver)

driver.get('https://findtreatment.gov/')
driver.maximize_window()
# location
element_location = driver.find_element(By.NAME, 'location')
element_location.click()
element_location.send_keys('10019')
sleep(1)
element_location.send_keys(Keys.ENTER)
sleep(2)

#button location
button = driver.find_element(By.XPATH, '/html/body/div/div/main/div[3]/div/div/div/form/button')
button.click()
sleep(2)

# Distance
sleep(2)
element_distance = driver.find_element(By.ID, 'distance')
element_distance.send_keys(Keys.ARROW_DOWN)
element_distance.send_keys(Keys.ARROW_DOWN)
element_distance.click()

# BeautifulSoup4
soup = bs(driver.page_source, 'html_parser')
soup.prettify()
