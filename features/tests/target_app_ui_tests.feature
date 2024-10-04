# Created by bbkam at 10/1/2024
Feature: Test for target app page

  Scenario: User is able to open Privacy Policy
    Given Open target app page
    And Store original window
    When  Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page is open
    And Close current window
    And Return to original window


