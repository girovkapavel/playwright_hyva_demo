from playwright.sync_api import Page
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

    # Очень простая проверка: мини‑корзина должна открыться, элемент виден
    assert page.locator(".minicart-wrapper").first.is_visible()

