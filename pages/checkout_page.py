from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Step One - Information Form
        self.first_name_field = page.locator("[data-test='firstName']")
        self.last_name_field = page.locator("[data-test='lastName']")
        self.postal_code_field = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.error_message = page.locator("[data-test='error']")

        # Step Two - Overview
        self.cart_items = page.locator(".cart_item")
        self.finish_button = page.locator("[data-test='finish']")

        # Complete - Success Page
        self.success_header = page.locator(".complete-header")

    def navigate_to_step_one(self):
        self.navigate_to("checkout-step-one.html")

    def fill_first_name(self, first_name: str):
        self.first_name_field.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.last_name_field.fill(last_name)

    def fill_postal_code(self, postal_code: str):
        self.postal_code_field.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()

    def complete_checkout_info(self, first_name: str = "Roya", last_name: str = "Valiyeva", postal_code: str = "1010"):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)
        self.click_continue()

    def verify_on_step_one(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    def verify_on_step_two(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    def verify_on_complete_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    def verify_checkout_form_fields_visible(self):
        expect(self.first_name_field).to_be_visible()
        expect(self.last_name_field).to_be_visible()
        expect(self.postal_code_field).to_be_visible()

    def verify_error_displayed(self, expected_text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)

    def verify_cart_items_count(self, expected_count: int):
        expect(self.cart_items).to_have_count(expected_count)

    def verify_order_success(self):
        expect(self.success_header).to_be_visible()
        expect(self.success_header).to_have_text("Thank you for your order!")