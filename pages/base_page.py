from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def open(self):
        self.page.goto(self.URL)
        
  #  def click(self, selector: str):
   #     self.page.locator(selector).first.click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).first.fill(text)

    #def get_text(self, selector: str):
     #   return self.page.locator(selector).first.inner_text()
     
    def search_product(self, search_icon: str, search_input: str, query: str):
       
        search = self.page.get_by_role("button", name=search_icon)
        search.click()
        self.page.fill(search_input, query)
        self.page.keyboard.press("Enter")
        
        

    def add_to_cart_on_pdp(self, query: str):
        self.search_product(self.ICON_SEARCH, self.SEARCH_INPUT, query) 
        products = self.page.locator(self.PRODUCT_LINK)
        products.first.wait_for(state="visible")
        products.first.click()
        add_to_cart_btn = self.page.locator(self.ADD_TO_CART_PDP)
        add_to_cart_btn.wait_for(state="visible")
        add_to_cart_btn.click()
    
