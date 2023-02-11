from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service('C:/Users/hgord/Documents/Careerist QA Automation/python-selenium-automation/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com')
driver.find_element(By.ID, 'nav-orders').click()

#I first tried to use the xpath $x("//h1[text()='Sign in']") to find sign in as there arent any great tags, can you
#explain why it didnt work?


assert driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").is_displayed(), 'Sign in text not visible'
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not visible'
