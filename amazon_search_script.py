from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service('C:/Users/hgord/Documents/Careerist QA Automation/python-selenium-automation/chromedriver.exe')
driver = webdriver.Chrome(service=service)



driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID, 'nav-search-submit-button').click()