def test_search(home):
    home.open_search()
    home.search("bag")

def test_whats_new(home):
    home.click_whats_new()

def test_women(home):
    home.click_women()

def test_men(home):
    home.click_men()

def test_shop(home):
    home.click_gear()

def test_training(home):
    home.click_training()

def test_sale(home):
    home.click_sale()

def test_add_to_cart_on_pdp(home):
    home.open()
    home.add_to_cart_on_pdp("bag")

def test_add_to_cart_on_plp(home):
    home.open()
    home.add_to_cart_on_plp("bag")

