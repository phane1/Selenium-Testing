from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import features.locators as locators
import features.steps.user_actions as action
import time

@when('the user looks at the header')
def step_user_looks_at_header(context):
    context.header = action.get_text(context, locators.homepage_header)

@when('the user looks at the footer')
def step_user_looks_at_footer(context):
    context.footer = action.get_text(context, locators.footer_message)

@then('the header will be correct')
def step_header_is_correct(context):
    assert "Swag Labs" == context.header, f"The header is NOT correct. Got {context.header} instead"
    context.browser.quit()

@then('the footer will be correct')
def step_footer_is_correct(context):
    # Assert that the footer message is correct
    assert "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy" == context.footer, f"The footer message is NOT correct. Got {context.footer} instead"

    # Assert that the Twitter logo is visible
    check_visible = action.verify_element_visible(context, locators.twitter_hyperlink)
    assert check_visible, "The Twitter logo hyperlink is NOT visible in the footer"

    # Assert that Facebook logo is visible
    check_visible = action.verify_element_visible(context, locators.facebook_hyperlink)
    assert check_visible, "The Facebook logo hyperlink is NOT visible in the footer"

    # Assert that LinkedIn logo is visible
    check_visible = action.verify_element_visible(context, locators.linkedin_hyperlink)
    assert check_visible, "The LinkedIn logo hyperlink is NOT visible in the footer"

    context.browser.quit()