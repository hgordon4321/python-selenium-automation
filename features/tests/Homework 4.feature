# Created by hgord at 2/24/2023
Feature: Homework 4


  Scenario: 1. Check links in bestsellers page
    Given Navigate to bestsellers page
    Then Verify there are 5 links in ribbon bar

#Did you say in class that test cases should always have all 3 step types?
#If so, for this case would it make sense to add a pointless user interaction to be a then step
#Or to split the steps differently (i.e. given open browser, when navigate to bs page, then verify)

  Scenario: 2. Add random product from main page to cart
    Given Open Amazon page
    When Main page product link is clicked
    And First product is selected
    And Product is added to cart
    Then Verify cart has 1 item