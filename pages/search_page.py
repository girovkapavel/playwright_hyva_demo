from playwright.sync_api import expect
from pages.base_page import BasePage

class SearchPage(BasePage):
 

    URL = "https://demo.hyva.io/"
    ICON_SEARCH = "Toggle search form"
    SEARCH_INPUT = "input[name='q']"
    
   
    def search_for_item(self, query: str):
        self.search_product(self.ICON_SEARCH, self.SEARCH_INPUT, query)