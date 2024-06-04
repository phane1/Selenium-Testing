# File that has user function actions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import features.locators as locators

def enter_username(context, username):
    context.browser.find_element(By .XPATH, locators.username_field).send_keys(username)

def enter_password(context, password):
    context.browser.find_element(By .XPATH, locators.password_field).send_keys(password)

def enter_firstname(context, firstname):
    context.browser.find_element(By .XPATH, locators.firstname_field).send_keys(firstname)

def enter_lastname(context, lastname):
    context.browser.find_element(By .XPATH, locators.lastname_field).send_keys(lastname)

def enter_zipcode(context, zipcode):
    context.browser.find_element(By .XPATH, locators.zipcode_field).send_keys(zipcode)

def click_button(context, button_locator):
    context.browser.find_element(By .XPATH, button_locator).click()

def get_text(context, text_locator):
    return context.browser.find_element(By .XPATH, text_locator).text

def hover_over_element(context, element_locator):
    element = context.browser.find_element(By .XPATH, element_locator)
    actions = ActionChains(context.browser)
    actions.move_to_element(element).perform()

def get_element(context, element_locator):
    return context.browser.find_element(By.XPATH, element_locator)

def verify_element_visible(context, element_locator):
    try:
        context.browser.find_element(By .XPATH, element_locator)
    except NoSuchElementException:
        return False
    return True