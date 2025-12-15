from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.locator(selector).first.click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).first.fill(text)

    def text(self, selector: str) -> str:
        return self.page.locator(selector).first.inner_text()
