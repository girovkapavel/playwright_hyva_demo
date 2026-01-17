import re
from playwright.sync_api import expect
from pages.base_page import BasePage



class CartPage(BasePage):
    URL = "https://demo.hyva.io/"
    PRODUCT_LINK = ".product-item-link"
    ADD_TO_CART_PDP = "#product-addtocart-button"

    MINICART_TOGGLE = "#menu-cart-icon"
    VIEW_CART_BUTTON = "text=View and Edit Cart"

    ICON_SEARCH = "Toggle search form"
    SEARCH_INPUT = "input[name='q']"

    

    def open_cart_from_pdp(self):
        self.add_to_cart_on_pdp("bag")
        minicart_btn = self.page.locator(self.MINICART_TOGGLE).first
        minicart_btn.wait_for(state="visible", timeout=3000)
        expect(minicart_btn).to_be_visible()    
        minicart_btn.click()
        self.page.locator(self.VIEW_CART_BUTTON).click()
        
            

    def input_discount(self):
        self.open_cart_from_pdp()
        self.page.locator("details.coupon-form > summary").click()
        self.page.get_by_placeholder("Enter discount code").fill("discount2024")
        self.page.get_by_role("button", name="Apply Discount").click()
        
        
        
    def change_quantity(self, quantity: str):
        self.open_cart_from_pdp()
        qty_input = self.page.get_by_role("spinbutton", name="Qty")
        qty_input.fill("2")
        quantity_input = self.page.locator("input.qty")
        quantity_input.fill(quantity)
        self.page.get_by_role("button", name="Update Shopping Cart").click()
        

    def remove_item_from_cart(self):
        self.open_cart_from_pdp()
        self.page.get_by_role("button", name=re.compile(r"^Remove")).first.click()
        
    
    def proceed_to_checkout(self):
        self.open_cart_from_pdp()
        self.page.get_by_role("link", name="Proceed to Checkout").click()
    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        