import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_products_page_displays_items(page: Page):  # ← NO spaces before "def"
    login_page = LoginPage(page)  # ← 4 spaces indent
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.verify_products_displayed(6)


def test_all_products_have_name(page: Page):  # ← NO spaces before "def"
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.verify_all_products_have_names()


def test_all_products_have_price(page: Page):  # ← NO spaces before "def"
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.verify_all_products_have_prices()


def test_all_products_have_add_to_cart_button(page: Page):  # ← NO spaces before "def"
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.verify_all_products_have_add_to_cart_buttons()


def test_all_products_have_images(page: Page):  # ← NO spaces before "def"
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.verify_all_products_have_images()


def test_clicking_product_opens_details(page: Page):  # ← NO spaces before "def"
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    product_name = products_page.get_first_product_name()
    products_page.click_first_product()
    products_page.verify_product_detail_page(product_name)


def test_products_have_descriptions(page: Page):  # ← NO spaces before "def"
    login_page = LoginPage(page)
    login_page.login_as_standard_user()

    products_page = ProductsPage(page)
    products_page.verify_all_products_have_descriptions()