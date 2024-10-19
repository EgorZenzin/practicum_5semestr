from src.pages.login_page import LoginPage

def test_display(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_title_visible()
    assert login_page.get_title_text() == "Products"
    
    page.close()
