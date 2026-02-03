import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart_icon_is_visible(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    cart_page = CartPage(page)
    cart_page.verify_cart_icon_visible()


def test_add_to_cart_updates_badge(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.verify_cart_badge_shows("1")


def test_add_multiple_items_to_cart(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()
    products_page.add_bike_light_to_cart()
    page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()

    cart_page = CartPage(page)
    cart_page.verify_cart_badge_shows("3")


def test_clicking_cart_opens_cart_page(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    cart_page = CartPage(page)
    cart_page.click_cart_icon()
    cart_page.verify_on_cart_page()


def test_added_item_appear_in_cart(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    product_name = products_page.get_first_product_name()
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.click_cart_icon()
    cart_page.verify_item_in_cart(product_name)


def test_remove_button_appears_after_add_to_cart(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")
    expect(remove_button).to_be_visible()
    expect(remove_button).to_have_text("Remove")


def test_remove_from_cart_updates_badge(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(page)
    cart_page.verify_cart_badge_shows("1")

    page.locator("[data-test='remove-sauce-labs-backpack']").click()
    cart_page.verify_cart_badge_not_visible()