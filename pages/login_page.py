from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

        self.username_field = page.locator("[data-test=\"username\"]")
        self.password_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

    def navigate(self):
        self.navigate_to("")

    def fill_username(self, username: str):
        self.username_field.fill(username)

    def fill_password(self, password: str):
        self.password_field.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def login_as_standard_user(self):
        self.navigate()
        self.login("standard_user", "secret_sauce")

    def verify_login_successful(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def verify_error_displayed(self, expected_text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)

    def verify_username_field_has_value(self, expected_value: str):
        expect(self.username_field).to_have_value(expected_value)

    def verify_password_field_has_value(self, expected_value: str):
        expect(self.password_field).to_have_value(expected_value)


