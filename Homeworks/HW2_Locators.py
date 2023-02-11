from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


#Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email field
driver.find_element(By.ID, 'ap_email')

#Continue button
driver.find_element(By.ID, 'continue')

#Need Help Link
driver.find_element(By.XPATH, "//a[contains(@data-csa-c-func-deps, 'a-expander-toggle')]")

#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Other issues with sign in link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#Create account button
driver.find_element(By.ID, 'createAccountSubmit')

#Conditions of use (middle, using container for practice)
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")
#Is above correct? I know first part is but cant check second due to the bug discussed in lesson 3

#Conditions of use link (footer)
driver.find_element(By.XPATH, "//a[contains(@href, 'desktop_footer_cou')]")

#Privacy notice (middle)
driver.find_element(By.XPATH, "//a[contains(@href, 'signin_notification_privacy_notice')]")
