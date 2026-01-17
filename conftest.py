import pytest
import webbrowser
from pathlib import Path
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.fixture
def home(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    home_page = HomePage(page)
    home_page.open()
    return home_page

@pytest.fixture
def cart(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    return CartPage(page)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = "report.html"


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    report_path = Path("report.html").resolve()
    if report_path.exists():
        webbrowser.open_new_tab(report_path.as_uri())
