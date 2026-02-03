from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.products = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.product_descriptions = page.locator(".inventory_item_desc")
        self.product_images = page.locator(".inventory_item img")
        self.add_to_cart_buttons = page.locator("[data-test^='add-to-cart']")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def navigate(self):
        self.navigate_to("inventory.html")

    def click_first_product(self):
        self.product_names.first.click()

    def get_first_product_name(self):
        return self.product_names.first.inner_text()

    def add_backpack_to_cart(self):
        self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    def add_bike_light_to_cart(self):
        self.page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()

    def verify_products_displayed(self, expected_count: int=6):
        expect(self.products).to_have_count(expected_count)

    def verify_all_products_have_names(self):
        names=self.product_names.all()
        for index, name in enumerate(names):
            expect(name).to_be_visible()
            name_text = name.inner_text()
            assert len(name_text) > 0, f"Product {index + 1} has no name!"

    def verify_all_products_have_prices(self):
        prices=self.product_prices.all()
        for index, price in enumerate(prices):
            expect(price).to_be_visible()
            price_text = price.inner_text()
            assert "$" in price_text, f"Product {index + 1} has no $ symbol!"

    def verify_all_products_have_add_to_cart_buttons(self):
        buttons = self.add_to_cart_buttons.all()
        assert len(buttons) == 6, "Should have 6 Add to Cart buttons"
        for button in buttons:
            expect(button).to_be_visible()
            expect(button).to_be_enabled()

    def verify_all_products_have_images(self):
        images=self.product_images.all()
        for index, image in enumerate(images):
            expect(image).to_be_visible()

    def verify_product_detail_page(self, product_name: str):
        self.page.wait_for_url("**/inventory-item.html**")
        detail_name = self.page.locator(".inventory_details_name")  # ← Change this line!
        expect(detail_name).to_contain_text(product_name)
        back_button = self.page.locator("[data-test='back-to-products']")
        expect(back_button).to_be_visible()

    def verify_all_products_have_descriptions(self):
        descriptions=self.product_descriptions.all()
        for index, description in enumerate(descriptions):
            expect(description).to_be_visible()
            desc_text = description.inner_text()
            assert len(desc_text) > 0, f"Product {index + 1} has no description!"
