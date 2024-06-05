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

    Scenario: Verify the sorting Name (Z to A) works successfully
        Given the user is on the home screen
        When the user changes the sorting to Name (Z to A)
        Then the items will be sorted from Z to A

    Scenario: Verify the sorting Name (A to Z) works successfully
        Given the user is on the home screen
        When the user changes the sorting to Name (A to Z)
        Then the items will be sorted from A to Z

    Scenario: Verify the sorting Price (low to high) works successfully
        Given the user is on the home screen
        When the user changes the sorting to Price (low to high)
        Then the items will be sorted from low to high

    Scenario: Verify the sorting Price (high to low) works successfully
        Given the user is on the home screen
        When the user changes the sorting the Price (high to low)
        Then the items will be sorted from high to low