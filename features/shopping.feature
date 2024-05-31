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