Feature: Test for main page UI

  Scenario: Verify hearder has correct amount links
    Given Open target main page
    Then  Verify header has 6 links



  Scenario: Verify header is shown
    Given Open target main page
    Then Verify header is shown
    And Verify header has links