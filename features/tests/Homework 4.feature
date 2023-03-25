# Created by hgord at 2/24/2023
Feature: Homework 4


  Scenario: 1. Check links in bestsellers page
    Given Navigate to bestsellers page
    Then Verify there are 5 links in ribbon bar

#Steps updated for HW7.2
  Scenario: 2. Add random product from main page to cart
    Given Open Amazon page
    When Main page product link is clicked
    And First product is selected
    And Product is added to cart
    Then Verify cart has 1 item

    # It seems like amazon made some changes to how the product group links on the main page work so I could no longer
    #select a random one, the test will break if the "Handbags" product group is no longer available when you check this