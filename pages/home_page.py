from playwright.sync_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://demo.hyva.io/"
    
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






    