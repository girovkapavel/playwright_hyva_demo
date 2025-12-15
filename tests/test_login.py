def test_login_failed(login_page):
    login_page.open_login()
    login_page.login("wrong@mail.com", "wrongpass")

    assert "Customer Login" in login_page.get_welcome_text()
