from behave import given, when, then
import features.locators as locators
import features.steps.user_actions as action
import time

@given('the user adds items to cart')
@when('the user adds items to cart')
def step_user_adds_items_to_cart(context):
    for add_button in locators.add_to_cart:
        action.click_button(context, add_button)
        time.sleep(1)

@when('the user removes items to cart')
def step_user_removes_items_from_cart(context):
    for remove_button in locators.remove_from_cart:
        action.click_button(context, remove_button)
        time.sleep(1)

@then('the number on the cart increments')
def step_number_on_cart_increments(context):
    cart_display_number = action.get_text(context, locators.cart_number)
    assert '6' == cart_display_number, f"The total does not match, got {cart_display_number} instead"
    context.browser.quit()

@then('the number on the cart decrements')
def step_number_on_cart_decrements(context):
    cart_display_number = action.get_text(context, locators.cart_number)
    assert '1' == cart_display_number, f"The total does not match, got {cart_display_number} instead"
    context.browser.quit()

@when('the user hovers over a hyperlink')
def step_user_overs_over_hyperlink(context):
    action.hover_over_element(context, locators.backpack_hyperlink)

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