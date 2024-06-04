# xPaths used in the automation

# Login Page Locators
username_field = "//input[@id='user-name']"
password_field = "//input[@id='password']"
login_button = "//input[@data-test='login-button']"
error_text = "//h3[@data-test='error']"
locked_text = "//h3[@data-test='error']"

# Hamburger Menu Locators
menu = "//button[@id='react-burger-menu-btn']"
about_option = "//a[text()='About']"
logout = "//a[text() = 'Logout']"

# Cart Related Locators
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
single_add_item = "(//button[text()='Add to cart'])[1]"
cart_number = "//span[@class='shopping_cart_badge']"
shopping_cart_button = "//a[@data-test='shopping-cart-link']"

# Checking Out Locators
checkout_button = "//button[@name='checkout']"
finish_button = "//button[@name='finish']"
thank_you_header = "//h2[@class='complete-header']"
dispatch_message = "//div[@class='complete-text']"
firstname_field = "//input[@name='firstName']"
lastname_field = "//input[@name='lastName']"
zipcode_field = "//input[@name='postalCode']"
continue_button = "//input[@name='continue']"

# Shopping UI Locators
backpack_hyperlink = "//div[text()='Sauce Labs Backpack']"
onesie_hyperlink = "//div[text()='Sauce Labs Onesie']"
homepage_header = "//div[@class='app_logo']"
twitter_hyperlink = "//a[@data-test='social-twitter']"
facebook_hyperlink = "//a[@data-test='social-facebook']"
linkedin_hyperlink = "//a[@data-test='social-linkedin']"
footer_message = "//div[@class='footer_copy']"