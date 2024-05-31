from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import features.locators as locators
import features.steps.user_actions as action
import time

@given('the user is on the login page')
def step_user_on_login_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.get('https://www.saucedemo.com/')

@given('the user is on the home screen')
def step_user_on_home_screen(context):
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.get('https://www.saucedemo.com/')
    action.enter_username(context, 'standard_user')
    action.enter_password(context, 'secret_sauce')
    action.click_button(context, locators.login_button)

@given('the user clicks the hamburger menu')
def step_user_clicks_on_hamnburger_menu(context):
    action.click_button(context, locators.menu)
    time.sleep(1)

@when('the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    action.enter_username(context, 'standard_user')
    action.enter_password(context, 'secret_sauce')
    action.click_button(context, locators.login_button)

@when('the user enters invalid credentials')
def step_user_enters_valid_credentials(context):
    action.enter_username(context, 'standard_user')
    action.enter_password(context, 'blahblahblah')
    action.click_button(context, locators.login_button)

@when('the user clicks the logout option')
def step_user_clicks_logout(context):
    action.click_button(context, locators.logout)

@when('the user enters a locked out account info')
def step_user_enters_locked_out_account(context):
    action.enter_username(context, 'locked_out_user')
    action.enter_password(context, 'secret_sauce')
    action.click_button(context, locators.login_button)

@then('the user is redirected to the inventory page')
def step_user_redirected_to_inventory(context):
    time.sleep(1)
    url = context.browser.current_url
    assert 'https://www.saucedemo.com/inventory.html' == url, f"The user was NOT redirected to the correct url, got {url} instead"
    context.browser.quit()

@then('the user is redirected to the login page')
def step_user_redirected_to_login(context):
    time.sleep(1)
    url = context.browser.current_url
    assert 'https://www.saucedemo.com/' == url, f"The user was NOT redirected to the correct url, got {url} instead"
    context.browser.quit()

@then('the user is not redirect to the inventory page')
def step_user_not_redirected_to_inventory(context):
    time.sleep(1)
    error_message = action.get_text(context, locators.error_text)
    assert 'Epic sadface: Username and password do not match any user in this service' == error_message, f"The error message is not correctly displayed, got {error_message} instead"
    url = context.browser.current_url
    assert 'https://www.saucedemo.com/' == url, f"The user was NOT redirected to the correct url, got {url} instead"
    context.browser.quit()

@then('the user will get the locked error message')
def step_user_will_get_locked_error_message(context):
    time.sleep(1)
    error_message = action.get_text(context, locators.locked_text)
    assert 'Epic sadface: Sorry, this user has been locked out.' == error_message, f"The error message is not correctly displayed, got {error_message} instead"
    url = context.browser.current_url
    assert 'https://www.saucedemo.com/' == url, f"The user was NOT redirected to the correct url, got {url} instead"
    context.browser.quit()