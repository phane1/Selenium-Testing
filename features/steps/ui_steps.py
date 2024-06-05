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

@when('the user changes the sorting to Name (Z to A)')
def step_user_changes_sorting_to_Z_to_A(context):
    # Changing the filter from A to Z to Z to A
    action.click_button(context, locators.filter)
    time.sleep(1)
    action.click_button(context, locators.z_to_a)
    time.sleep(1)

    # Initializing an empty array
    context.items = []
    # For loop that goes from 1 to 6
    for x in range(1,7):
        # Returns the text of the item that is currently selected
        item_name = action.get_text(context, locators.item+"["+ str(x) +"]")
        # and puts it into an array
        context.items.append(item_name)

@when('the user changes the sorting to Name (A to Z)')
def step_user_changes_sorting_to_A_to_Z(context):
    # Changing the filter from A to Z to Z to A back to A to Z
    # Note: need to do that to make sure the filter option does work
    action.click_button(context, locators.filter)
    time.sleep(1)
    action.click_button(context, locators.z_to_a)
    time.sleep(1)
    action.click_button(context, locators.filter)
    time.sleep(1)
    action.click_button(context, locators.a_to_z)
    time.sleep(1)

    # Initializing an empty array
    context.items = []
    # For loop that goes from 1 to 6
    for x in range(1,7):
        # Returns the text of the item that is currently selected
        item_name = action.get_text(context, locators.item+"["+ str(x) +"]")
        # and puts it into an array
        context.items.append(item_name)

@when('the user changes the sorting to Price (low to high)')
def step_user_changes_sorting_to_low_to_high(context):
    # Changing the filter from A to Z to low to high
    action.click_button(context, locators.filter)
    time.sleep(1)
    action.click_button(context, locators.low_to_hi)
    time.sleep(1)

    # Initialzing two empty arrays
    # One to hold item name and the other to hold item prices
    context.items = []
    context.item_prices = []
    # For loop that goes from 1 to 6
    for x in range(1,7):
        # Returns the text & price of the item that is currently selected
        item_name = action.get_text(context, locators.item+"["+ str(x) +"]")
        item_price = action.get_text(context, locators.item_price+"["+ str(x) +"]")
        # and puts it into item array
        context.items.append(item_name)
        context.item_prices.append(item_price)

@when('the user changes the sorting the Price (high to low)')
def step_user_changes_the_sdorting_to_high_to_low(context):
    # Changing the filter from A to Z to high to low
    action.click_button(context, locators.filter)
    time.sleep(1)
    action.click_button(context, locators.hi_to_low)
    time.sleep(1)

    # Initialzing two empty arrays
    # One to hold item name and the other to hold item prices
    context.items = []
    context.item_prices = []
    # For loop that goes from 1 to 6
    for x in range(1,7):
        # Returns the text & price of the item that is currently selected
        item_name = action.get_text(context, locators.item+"["+ str(x) +"]")
        item_price = action.get_text(context, locators.item_price+"["+ str(x) +"]")
        # and puts it into item array
        context.items.append(item_name)
        context.item_prices.append(item_price)


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

@then('the items will be sorted from Z to A')
def step_items_will_be_sorted_z_to_a(context):
    # Creating an array to check with the built array from earlier
    check = [
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Onesie",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Bike Light",
        "Sauce Labs Backpack"
    ]

    # For loop that goes from positions 0 to 5
    for x in range(6):
        # Print the current item in the array
        print(check[x])
        print(context.items[x])
        # If the items match then it is correct, else sends an error message
        assert check[x] == context.items[x], f"It is NOT sorted in the correct order. Got {context.arr[x]} instead of {check[x]}"

    context.browser.quit()

@then('the items will be sorted from A to Z')
def step_items_will_be_sorted_a_to_z(context):
    # Creating an array to check with the built array from earlier
    check = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]

    # For loop that goes from positions 0 to 5
    for x in range(6):
        # Print the current item in the array
        print(check[x])
        print(context.items[x])
        # If the items match then it is correct, else sends an error message
        assert check[x] == context.items[x], f"It is NOT sorted in the correct order. Got {context.arr[x]} instead of {check[x]}"

    context.browser.quit()

@then('the items will be sorted from low to high')
def step_items_will_be_sorted_low_to_high(context):
    # Creating an array of itme names to check with the built array from earlier
    check_name = [
        "Sauce Labs Onesie",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Backpack",
        "Sauce Labs Fleece Jacket"
    ]
    # Creating an array of prices to check with the built array from earlier
    check_price = [
        "$7.99",
        "$9.99",
        "$15.99",
        "$15.99",
        "$29.99",
        "$49.99"
    ]

    # For loop that goes from positions 0 to 5
    for x in range(6):
        # Print the current item in the array
        print(check_name[x])
        print(context.items[x])
        print(check_price[x])
        print(context.item_prices[x])
        # If the item names match then it is correct, else sends an error message
        assert check_name[x] == context.items[x], f"It is NOT sorted in the correct order. Got {context.arr[x]} instead of {check_name[x]}"
        # If the item prices match then it is correct, else sends an error message
        assert check_price[x] == context.item_prices[x], f"It is NOT sorted in the correct order. Got {context.item_prices[x]} instead of {check_price[x]}"

    context.browser.quit()

@then('the items will be sorted from high to low')
def step_items_will_be_sorted_low_to_high(context):
    # Creating an array of itme names to check with the built array from earlier
    check_name = [
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bike Light",
        "Sauce Labs Onesie"
    ]
    # Creating an array of prices to check with the built array from earlier
    check_price = [
        "$49.99",
        "$29.99",
        "$15.99",
        "$15.99",
        "$9.99",
        "$7.99"
    ]

    # For loop that goes from positions 0 to 5
    for x in range(6):
        # Print the current item in the array
        print(check_name[x])
        print(context.items[x])
        print(check_price[x])
        print(context.item_prices[x])
        # If the item names match then it is correct, else sends an error message
        assert check_name[x] == context.items[x], f"It is NOT sorted in the correct order. Got {context.arr[x]} instead of {check_name[x]}"
        # If the item prices match then it is correct, else sends an error message
        assert check_price[x] == context.item_prices[x], f"It is NOT sorted in the correct order. Got {context.item_prices[x]} instead of {check_price[x]}"

    context.browser.quit()