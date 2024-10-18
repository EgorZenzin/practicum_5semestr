from src.pages.login_page import LoginPage

def test_login_positive(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    page.close()
