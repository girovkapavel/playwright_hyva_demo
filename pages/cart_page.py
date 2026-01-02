from pages.home_page import HomePage
from playwright.sync_api import expect

class CartPage:
    MINICART_TOGGLE = ".action.showcart"

    def __init__(self, page):
        self.page = page
        self.home = HomePage(page)

    def open_cart_with_one_product(self):
        self.home.open_search()
        self.home.search("bag")
        self.home.add_first_product_to_cart_from_plp()

        minicart = self.page.locator(self.MINICART_TOGGLE).first
        minicart.wait_for(state="visible")
        minicart.click()
