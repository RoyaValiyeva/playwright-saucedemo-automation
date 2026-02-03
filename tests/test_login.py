import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage



def test_login_page_loads(page: Page):
    login_page=LoginPage(page)
    login_page.navigate()
    expect(page).to_have_title("Swag Labs")

def test_successful_login_with_standard_user(page: Page):
    login_page = LoginPage(page)
    login_page.login_as_standard_user()
    login_page.verify_login_successful()
    products = page.locator(".inventory_item")
    expect(products.first).to_be_visible()

def test_login_with_wrong_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login ("standard_user", "wrong_password")
    login_page.verify_error_displayed("Username and password do not match")

def test_login_with_empty_username(page: Page):
    login_page=LoginPage(page)
    login_page.navigate()
    login_page.fill_password("secret_sauce")
    login_page.click_login()
    login_page.verify_error_displayed("Username is required")

def test_login_with_empty_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.fill_username("standard_user")
    login_page.click_login()
    login_page.verify_error_displayed("Password is required")

def test_username_field_accepts_input(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.fill_username("testuser")
    login_page.verify_username_field_has_value("testuser")

def test_password_field_accepts_input(page: Page):
    login_page=LoginPage(page)
    login_page.navigate()
    login_page.fill_password("wrongpassword")
    login_page.verify_password_field_has_value("wrongpassword")




