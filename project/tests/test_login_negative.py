from src.pages.login_page import LoginPage

def test_login_negative(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    
    login_page = LoginPage(page)
    login_page.login("invalid_user", "invalid_password")

    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"
    
    page.close()
