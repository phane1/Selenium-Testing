# Testing the Home Page UI as a User

Feature: Home Page UI

    Scenario: Verify the home page header is correct
        Given the user is on the home screen
        When the user looks at the header
        Then the header will be correct

    Scenario: Verify the home page footer is correct
        Given the user is on the home screen
        When the user looks at the footer
        Then the footer will be correct