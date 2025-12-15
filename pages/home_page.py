from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://demo.hyva.io/"

    SEARCH_TOGGLE = "button[aria-label='Toggle search form']"
    SEARCH_INPUT = "input[name='q']"
    FIRST_PRODUCT = ".product-item-link"
    PRODUCT_LINK = ".product-item-link"

    WOMEN_LINK = "https://demo.hyva.io/default/women.html"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.goto(self.URL)

    def open_search(self):
        self.click(self.SEARCH_TOGGLE)

    def search(self,query: str):
        self.fill(self.SEARCH_INPUT, query)
        self.page.keyboard.press("Enter")

    def open_first_product(self):
        self.page.locator(self.FIRST_PRODUCT).first.click()

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
        add_to_cart_btn = self.page.locator("#product-addtocart-button")
        add_to_cart_btn.wait_for(state="visible")

        # Добавляем в корзину
        add_to_cart_btn.click()

    def add_to_cart_on_plp(self, query: str):
        self.open_search()
        self.search(query)
        self.page.get_by_role("button", name="Add to Cart").first.click()









