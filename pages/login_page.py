from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    URL = "https://demo.hyva.io/default/customer/account/login/"

    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#pass"
    PAGE_TITLE = ".page-title"
    
    
    FIRSTNAME_INPUT = "#firstname"
    LASTNAME_INPUT = "#lastname"
    PASSWORD_CONFIRM_INPUT = "#password-confirmation"
    PASSWORD_INPUT_REGISTRATION = "#password"
    EMAIL_INPUT_REGISTRATION = "#email_address"
    
    
    ERROR_MESSAGE = "There is already an account with this email address"
    
    def login(self, email: str, password: str):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.page.get_by_role("button", name="Sign In").click()
        expect(self.page).to_have_url("https://demo.hyva.io/default/customer/account/")

        self.page.get_by_role("link", name="Sign Out").click()

    def forgot_password(self):
        self.page.get_by_role("link", name="Create an Account").click()
        
    def register_account(self, email: str, password: str, firstname: str, lastname: str):
        self.page.get_by_role("link", name="Create an Account").click()
        self.fill(self.FIRSTNAME_INPUT, firstname)
        self.fill(self.LASTNAME_INPUT, lastname)
        self.fill(self.EMAIL_INPUT_REGISTRATION, email)
        self.fill(self.PASSWORD_INPUT_REGISTRATION, password)
        self.fill(self.PASSWORD_CONFIRM_INPUT, password)
        self.page.get_by_role("button", name="Create an Account").click()

        expect(self.page.get_by_text(self.ERROR_MESSAGE)).to_contain_text(self.ERROR_MESSAGE)       
        
        
        
        
        