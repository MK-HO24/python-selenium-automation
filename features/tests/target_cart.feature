Feature: Test for target cart feature

  Scenario: User can verify empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty



  Scenario: User can verify cart is not empty
    Given Open target main page
    When Search for shoes
    And Add first search result to cart
    And Open target cart page
    Then Verify cart is not empty
