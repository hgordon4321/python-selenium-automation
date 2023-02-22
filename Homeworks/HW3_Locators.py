from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# Logo
driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')

# Create account text
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Name field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password field
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# Password info bar
driver.find_element(By.CSS_SELECTOR, "div.a-alert-inline[aria-live='polite'")
# If there is a much better selector for this please let me know, I could not find one

# Re-enter password field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Create account button (reads continue for me)
driver.find_element(By.CSS_SELECTOR, '#continue')

# Conditions of use link
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

# Privacy notice link
driver.find_element(By.CSS_SELECTOR, "a[href*='register_notification_privacy_notice']")

# Sign in link
driver.find_element(By.CSS_SELECTOR, "a[href*='signin']")