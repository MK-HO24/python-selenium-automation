# Created by bbkam at 9/13/2024
Feature: Test for target search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Search for a product
    Then Verify that correct result shown


  Scenario: User can verify empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty


  Scenario:  user can navigate to Sign In
    Given Open target main page
    When Click on Sign in icon
    When Click Sign in Right Nav Menu
    Then Verify Sign In form opened