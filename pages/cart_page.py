from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.remove_buttons = page.locator("[data-test^='remove']")

    def navigate(self):
        self.navigate_to("cart.html")

    def click_cart_icon(self):
        self.cart_link.click()

    def click_checkout(self):
        self.checkout_button.click()

    def verify_cart_icon_visible(self):
        expect(self.cart_link).to_be_visible()

    def verify_on_cart_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")

    def verify_cart_badge_shows(self, count: str):
        expect(self.cart_badge).to_be_visible()
        expect(self.cart_badge).to_have_text(count)

    def verify_cart_badge_not_visible(self):
        expect(self.cart_badge).not_to_be_visible()

    def verify_item_in_cart(self, product_name: str):
        expect(self.cart_items).to_be_visible()
        expect(self.cart_items).to_contain_text(product_name)

    def verify_checkout_button_visible(self):
        expect(self.checkout_button).to_be_visible()
        expect(self.checkout_button).to_have_text("Checkout")