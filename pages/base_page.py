from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.base_url= "https://www.saucedemo.com/"

    def navigate_to(self, path: str= ""):
        url = f"{self.base_url}{path}"
        self.page.goto(url)

    def wait_for_url(self, url: str):
        expect(self.page).to_have_url(url)


