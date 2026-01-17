


def test_add_to_cart_on_pdp(cart):
    cart.open()
    cart.add_to_cart_on_pdp("bag")



def test_open_cart_from_pdp(cart):
    cart.open()
    cart.open_cart_from_pdp()
    

def test_input_discount(cart):
    cart.open()
    cart.input_discount() 
    
    
    
def test_change_quantity(cart):
    cart.open()
    cart.change_quantity("2")
    

def test_remove_item_from_cart(cart):
    cart.open()
    cart.remove_item_from_cart()    
    
def test_proceed_to_checkout(cart):
    cart.open()
    cart.proceed_to_checkout()



    
    


