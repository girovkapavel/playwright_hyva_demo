from playwright.sync_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://demo.hyva.io/"

    SEARCH_TOGGLE = "button[aria-label='Toggle search form']"
    SEARCH_INPUT = "input[name='q']"

    PRODUCT_LINK = ".product-item-link"
    ADD_TO_CART_PDP = "#product-addtocart-button"

    MINICART_TOGGLE = ".action.showcart"
    VIEW_CART_LINK = "a.action.viewcart"

    def open(self):
        self.goto(self.URL)

    def open_search(self):
        toggle = self.page.locator(self.SEARCH_TOGGLE)
        toggle.wait_for(state="visible")
        toggle.click()

    def search(self, query: str):
        self.fill(self.SEARCH_INPUT, query)
        self.page.keyboard.press("Enter")

    def open_first_product(self):
        product = self.page.locator(self.PRODUCT_LINK).first
        product.wait_for(state="visible")
        product.click()

    def click_whats_new(self):
        self.page.get_by_role("link", name="What's New").click()

    def click_women(self):
        self.page.get_by_role("link", name="Women").click()

    def click_men(self):
        self.page.get_by_role("link", name="Men", exact=True).click()

    def click_gear(self):
        self.page.get_by_role("link", name="Gear").click()

    def click_training(self):
        self.page.get_by_role("link", name="Training").click()

    def click_sale(self):
        self.page.get_by_role("link", name="Sale").click()

    def add_to_cart_on_pdp(self, query: str):
        self.open_search()
        self.search(query)

        # Ждём появления списка товаров (PLP)
        products = self.page.locator(self.PRODUCT_LINK)
        products.first.wait_for(state="visible")

        # Переходим на первый товар
        products.first.click()

        # Ждём полную загрузку PDP
        add_to_cart_btn = self.page.locator(self.ADD_TO_CART_PDP)
        add_to_cart_btn.wait_for(state="visible")

        # Добавляем в корзину
        add_to_cart_btn.click()

    def add_to_cart_on_plp(self, query: str):
        self.open_search()
        self.search(query)
        button = self.page.get_by_role("button", name="Add to Cart").first
        button.wait_for(state="visible")
        button.click()

    def open_cart_from_header(self):
        # Открыть мини-корзину и перейти в полную корзину
        self.page.locator(self.MINICART_TOGGLE).first.click()
        # На Hyvä появляется дропдаун с ссылкой View Cart / Go to Checkout
        # Пробуем кликнуть по ссылке View Cart, иначе fallback — прямой переход
        view_cart = self.page.locator(self.VIEW_CART_LINK)
        if view_cart.count() > 0:
            view_cart.first.click()
        else:
            self.page.goto("https://demo.hyva.io/checkout/cart/")

    def add_first_product_to_cart_from_plp(self):
        add_button = self.page.locator("button[title='Add to Cart']").first
        add_button.wait_for(state="visible")
        add_button.click()

        # Hyvä меняет текст кнопки после добавления
        expect(add_button).to_have_text("Added")
