# Created by HGordon at 3/30/2023
Feature: Homework 8
  # Enter feature description here

  Scenario: 1. Search filtering by type
    Given Open Amazon page
    When Filter search to Industrial & Scientific
    And Enter Glove in search box
    And Click on search icon
    Then Store name of product number 1
    When Filter search to Clothing, Shoes & Jewelry
    And Click on search icon
    Then Store name of product number 1
    And Verify product names are different


  Scenario: 2. Popup appears for New Arrivals hover
    Given Navigate to product page: https://www.amazon.com/gp/product/B074TBCSC8
    When Hover over new arrivals
    Then Verify deals appear
