from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_search_and_add_to_cart(page: Page):
    home = HomePage(page)
    home.open()
    home.open_search()
    home.search("Bag")
    home.open_first_product()

    product = ProductPage(page)
    product.add_to_cart()
    product.open_cart()

    # Проверяем, что мини‑корзина открылась
    expect(page.locator(".minicart-wrapper").first).to_be_visible()
