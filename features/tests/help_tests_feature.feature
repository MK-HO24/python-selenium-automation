Feature: To test Help pages

  Scenario: User can select help topic Promotion and Coupons
    Given Open Help page for return
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User can select help topic Target Circle
    Given Open Help page for return
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened


  Scenario: User can select help topic Compliance
    Given Open Help page for return
    Then Verify help Returns page opened
    When Select Help topic Compliance
    Then Verify help CA Abandoned Shopping Cart Retrieval page opened