import pytest
import webbrowser
from pathlib import Path
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage



@pytest.fixture
def home(page):
    home_page = HomePage(page)
    home_page.open()
    return home_page

@pytest.fixture
def login(page):
    login_page = LoginPage(page)
    login_page.open()
    return login_page

@pytest.fixture
def search(page):
    search_page = SearchPage(page)
    search_page.open()
    return search_page


@pytest.fixture
def cart(page):
    return CartPage(page)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = "report.html"


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    report_path = Path("report.html").resolve()
    if report_path.exists():
        webbrowser.open_new_tab(report_path.as_uri())
