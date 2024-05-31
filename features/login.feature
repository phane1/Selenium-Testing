# Testing the login functionality as a User

Feature: Login/Log out functionality

    Scenario: Verify when the user enters correct info, they can log in succesfully
        Given the user is on the login page
        When the user enters valid credentials
        Then the user is redirected to the inventory page

    Scenario: Verify when the user enters wrong info, they do not log in successfully
        Given the user is on the login page
        When the user enters invalid credentials
        Then the user is not redirect to the inventory page

    Scenario: Verify when the user clicks the log out button, they are logged out succesfully
        Given the user is on the home screen
        And the user clicks the hamburger menu
        When the user clicks the logout option
        Then the user is redirected to the login page

    Scenario: Verify when the user enters a locked out account's info, they get an error message
        Given the user is on the login page
        When the user enters a locked out account info
        Then the user will get the locked error message