def test_open_cart_with_one_product(cart):
    cart.open_cart_with_one_product()
    # Можно добавить проверку, что товар добавлен
    assert cart.page.locator(".cart.item").count() > 0
    
    #test_ 