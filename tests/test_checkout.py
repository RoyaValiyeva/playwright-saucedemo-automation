import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_button_is_visible(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.click_cart_icon()
    cart_page.verify_checkout_button_visible()


def test_clicking_checkout_opens_info_page(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.click_cart_icon()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.verify_on_step_one()
    checkout_page.verify_checkout_form_fields_visible()


def test_checkout_with_valid_information(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.click_cart_icon()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.complete_checkout_info("Roya", "Valiyeva", "1010")
    checkout_page.verify_on_step_two()
    checkout_page.verify_cart_items_count(1)


def test_checkout_with_empty_first_name_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.click_cart_icon()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_last_name("Valiyeva")
    checkout_page.fill_postal_code("1010")
    checkout_page.click_continue()
    checkout_page.verify_error_displayed("First Name is required")


def test_complete_checkout_flow(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.click_cart_icon()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.complete_checkout_info("Roya", "Valiyeva", "1010")
    checkout_page.verify_on_step_two()

    checkout_page.click_finish()
    checkout_page.verify_on_complete_page()
    checkout_page.verify_order_success()