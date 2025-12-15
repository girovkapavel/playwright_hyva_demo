import pytest
from pages.home_page import HomePage


@pytest.fixture
def home(page):
    home_page = HomePage(page)
    home_page.open()
    return home_page

