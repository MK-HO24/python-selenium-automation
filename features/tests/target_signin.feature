Feature: Test for target signin feature

  Scenario:  user can navigate to Sign In
    Given Open target main page
    When Click on Sign in icon
    When Click Sign in Right Nav Menu
    Then Verify Sign In form opened


  Scenario:  user can Sign In to account
    Given Open target main page
    When Click on Sign in icon
    When Click Sign in Right Nav Menu
    Then Verify Sign In form opened
    When Input user name
    When Input password
    When Click signin button
    Then Verify user is logged in


   Scenario:  user receives error message with wrong signin info
    Given Open target main page
    When Click on Sign in icon
    When Click Sign in Right Nav Menu
    Then Verify Sign In form opened
    When Input incorrect user name
    When Input incorrect password
    When Click signin button
    Then Verify error messge is displayed