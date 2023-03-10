# Created by hgord at 3/9/2023
Feature: Homework 6


  Scenario: User can open and close Amazon Privacy Notice
     Given Open Amazon T&C page
     When Click on Amazon Privacy Notice link
     And Switch to the newly opened window
     Then Verify Amazon Privacy Notice page is opened
     And User can close new window and switch back to original


#I skipped the storing original window and instead rechecked the windows to switch back