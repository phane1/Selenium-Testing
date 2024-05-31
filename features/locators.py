# xPaths used in the automation

# Login Page Locators
username_field = "//input[@id='user-name']"
password_field = "//input[@id='password']"
login_button = "//input[@data-test='login-button']"
error_text = "//h3[@data-test='error']"
menu = "//button[@id='react-burger-menu-btn']"
logout = "//a[text() = 'Logout']"
locked_text = "//h3[@data-test='error']"
add_to_cart = [
    "//button[@name='add-to-cart-sauce-labs-backpack']",
    "//button[@name='add-to-cart-sauce-labs-bike-light']",
    "//button[@name='add-to-cart-sauce-labs-bolt-t-shirt']",
    "//button[@name='add-to-cart-sauce-labs-fleece-jacket']",
    "//button[@name='add-to-cart-sauce-labs-onesie']",
    "//button[@name='add-to-cart-test.allthethings()-t-shirt-(red)']"
]
remove_from_cart = [
    "//button[@name='remove-sauce-labs-backpack']",
    "//button[@name='remove-sauce-labs-bike-light']",
    "//button[@name='remove-sauce-labs-bolt-t-shirt']",
    "//button[@name='remove-sauce-labs-fleece-jacket']",
    "//button[@name='remove-sauce-labs-onesie']"
]
cart_number = "//span[@class='shopping_cart_badge']"
backpack_hyperlink = "//div[text()='Sauce Labs Backpack']"
onesie_hyperlink = "//div[text()='Sauce Labs Onesie']"