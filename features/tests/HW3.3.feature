# Created by hgord at 2/21/2023
Feature: Amazon cart contents check-

#Steps updated for HW7.1.2
  Scenario: Empty cart check
    Given Open Amazon page
    When Click cart icon
    Then Verify "Cart is empty" appears
