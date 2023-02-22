# Created by hgord at 2/21/2023
Feature: Amazon sign in redirect


  Scenario: User clicks orders in nav bar
    Given Open Amazon page
    When Click on returns & orders
    Then Verify sign in page launches
