def test_add_to_cart(home_page, product_page, cart_page):
    home_page.open_home()
    home_page.click_search()
    home_page.search("Bag")
    home_page.open_first_product()

    product_page.add_to_cart()
    product_page.open_cart()

    cart_page.assert_cart_not_empty()