# Testing the shopping functionality as a User

Feature: Shopping functionality

    Scenario: Verify when user clicks the "Add to cart" button, the number on the cart increments
        Given the user is on the home screen
        When the user adds items to cart
        Then the number on the cart increments

    Scenario: Verify when user clicks the "Remove" button, the number on the cart decrements
        Given the user is on the home screen
        And the user adds items to cart
        When the user removes items to cart
        Then the number on the cart decrements

    Scenario: Verify when user hovers over a hyperlink, the text color changes
        Given the user is on the home screen
        When the user hovers over a hyperlink
        Then the text color changes

    Scenario: Verify user is able to checkout successfully
        Given the user is on the home screen
        And the user adds an item to cart
        And the user views the cart
        And the user clicks the checkout button
        And the user enters their information
        When the user clicks the finish button
        Then the user will be able to checkout successfully

    Scenario: Verify user is redirected to the Sauce Labs website when clicking the About
        Given the user is on the home screen
        And the user clicks the hamburger menu
        When the user clicks the About option
        Then the user will be redirected to Sauce Labs