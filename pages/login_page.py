from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://demo.hyva.io/customer/account/login/"

    EMAIL = "#email"
    PASSWORD = "#pass"
    LOGIN_BUTTON = "button[type='submit']"
    WELCOME_MSG = ".page-title"

    def open_login(self):
        self.open(self.URL)

    def login(self, email: str, password: str):
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_welcome_text(self) -> str:
        return self.get_text(self.WELCOME_MSG)
