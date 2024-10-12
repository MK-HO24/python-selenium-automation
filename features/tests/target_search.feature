Feature: Test for target search functionality

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify that correct result show coffee
    Then Verify that product coffee in URL

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify that correct result show tea
    Then Verify that product tea in URL

  Scenario Outline: User can search for product
    Given Open target main page
    When Search for <product>
    Then Verify that correct result show <expected_product>
    Examples:
    |product   |expected_product|
    |coffee    |coffee          |
    |tea       |tea             |
    |mug       |mug             |


  Scenario: User can see favorite tool tip for search result
    Given Open target main page
    When Search for umbrella
    And Hover favorite icon
    Then favorite tool tip is shown







