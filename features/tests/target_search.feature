# Created by bbkam at 9/13/2024
Feature: Test for target search functionality

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify that correct result show coffee

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify that correct result show tea

  Scenario Outline: User can search for product
    Given Open target main page
    When Search for <product>
    Then Verify that correct result show <expected_product>
    Examples:
    |product   |expected_product|
    |coffee    |coffee          |
    |tea       |tea             |
    |mug       |mug             |


