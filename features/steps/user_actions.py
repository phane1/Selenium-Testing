# File that has user function actions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import features.locators as locators

def enter_username(context, username):
    context.browser.find_element(By .XPATH, locators.username_field).send_keys(username)

def enter_password(context, password):
    context.browser.find_element(By .XPATH, locators.password_field).send_keys(password)

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