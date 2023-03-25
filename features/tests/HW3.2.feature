# Created by hgord at 2/21/2023
Feature: Amazon sign in redirect

#Steps updated for HW7.1.1
  Scenario: User clicks orders in nav bar
    Given Open Amazon page
    When Click on returns & orders
    Then Verify sign in page launches
