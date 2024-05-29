from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import features.locators as locators
import time

@given('the user is on the login page')
def step_user_on_login_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.get('https://www.saucedemo.com/')

@when('the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    context.browser.find_element(By .XPATH, locators.username_field).send_keys('standard_user')
    context.browser.find_element(By .XPATH, locators.password_field).send_keys('secret_sauce')
    context.browser.find_element(By .XPATH, locators.login_button).click()

@then('the user is redirected to the inventory')
def step_user_redirected_to_inventory(context):
    time.sleep(1)
    url = context.browser.current_url
    assert 'https://www.saucedemo.com/inventory.html' == url, "The user was NOT redirected to the correct url"
    context.browser.quit()