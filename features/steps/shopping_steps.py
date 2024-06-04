from behave import given, when, then
import features.locators as locators
import features.steps.user_actions as action
import time

@given('the user adds items to cart')
@when('the user adds items to cart')
def step_user_adds_items_to_cart(context):
    # Adding all the items into cart
    for add_button in locators.add_to_cart:
        action.click_button(context, add_button)
        time.sleep(1)

@given('the user adds an item to cart')
def step_user_adds_single_item_to_cart(context):
    # Adding a single item to cart
    action.click_button(context, locators.single_add_item)
    time.sleep(1)

@given('the user views the cart')
def step_user_views_cart(context):
    # Clicking the view cart button
    action.click_button(context, locators.shopping_cart_button)
    time.sleep(1)

@given('the user clicks the checkout button')
def step_user_clicks_checkout_button(context):
    # Clicking the checkout button
    action.click_button(context, locators.checkout_button)
    time.sleep(1)

@given('the user enters their information')
def step_user_enters_info(context):
    # Inputting all the user's information
    action.enter_firstname(context, 'foo')
    action.enter_lastname(context, 'bar')
    action.enter_zipcode(context, '92610')
    # Clicking the continue button
    action.click_button(context, locators.continue_button)

@when('the user removes items to cart')
def step_user_removes_items_from_cart(context):
    # Removing items from cart
    for remove_button in locators.remove_from_cart:
        action.click_button(context, remove_button)
        time.sleep(1)

@when('the user clicks the About option')
def step_user_clicks_about_option(context):
    # Clicking the about option in the hamburger menu
    action.click_button(context, locators.about_option)
    time.sleep(1)

@when('the user hovers over a hyperlink')
def step_user_overs_over_hyperlink(context):
    # Hovering over the title of an item on the home screen
    action.hover_over_element(context, locators.backpack_hyperlink)

@when('the user clicks the finish button')
def step_user_clicks_finish_button(context):
    # Clicking the finish button
    action.click_button(context, locators.finish_button)

@then('the number on the cart increments')
def step_number_on_cart_increments(context):
    # Making sure the correct number is shown on the cart
    cart_display_number = action.get_text(context, locators.cart_number)

    # Assert the correct number is shown
    assert '6' == cart_display_number, f"The total does not match, got {cart_display_number} instead"
    context.browser.quit()

@then('the number on the cart decrements')
def step_number_on_cart_decrements(context):
    # Making sure the correct number is shown on the cart
    cart_display_number = action.get_text(context, locators.cart_number)

    # Assert the correct number is shown
    assert '1' == cart_display_number, f"The total does not match, got {cart_display_number} instead"
    context.browser.quit()

@then('the text color changes')
def step_text_color_changes(context):

    # Locate the hyperlink elements again to get their CSS properties
    backpack_hyperlink_element = action.get_element(context, locators.backpack_hyperlink)
    onesie_hyperlink_element = action.get_element(context, locators.onesie_hyperlink)

    # Get the CSS properties
    hover_color = backpack_hyperlink_element.value_of_css_property("color")
    print(f"The color after hovering is: {hover_color}")
    standard_color = onesie_hyperlink_element.value_of_css_property("color")
    print(f"The standard color is: {standard_color}")

    # Assert that the colors are different
    assert hover_color != standard_color, f"The hover color ({hover_color}) did not change compared to the standard color ({standard_color})"

    context.browser.quit()

@then('the user will be able to checkout successfully')
def step_checkout_successfully(context):
    time.sleep(1)
    # Getting the text from the header
    header = action.get_text(context, locators.thank_you_header)
    # Assert that the header message is correct
    assert 'Thank you for your order!' == header, f'The header message is NOT correct. Got {header} instead'

    # Getting the text from the dispatch message
    dispatch = action.get_text(context, locators.dispatch_message)
    # Assert that the dispatch message is correct
    assert 'Your order has been dispatched, and will arrive just as fast as the pony can get there!' == dispatch, f'The dispatch message is NOT correct. Got {dispatch} instead'
    context.browser.quit()

@then('the user will be redirected to Sauce Labs')
def step_user_redirected_sauuce_labs(context):
    # Getting the current URL
    url = context.browser.current_url
    # Assert that the currenty url is correct
    assert 'https://saucelabs.com/' == url, f"The user was NOT redirected to the correct url, got {url} instead"

    context.browser.quit()