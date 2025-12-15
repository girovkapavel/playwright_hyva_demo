from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    CART_ITEM = ".product-item-name"

    def assert_cart_not_empty(self):
        locator = self.page.locator(self.CART_ITEM)
        locator.wait_for(state="visible")
        expect(locator).to_be_visible()
