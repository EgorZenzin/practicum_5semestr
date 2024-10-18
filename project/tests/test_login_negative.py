def test_login_negative(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("input#user-name", "invalid_user")
    page.fill("input#password", "invalid_password")
    page.click("input.btn_action")

    error_message = page.inner_text("h3[data-test='error']")
    assert error_message == "Epic sadface: Username and password do not match any user in this service"
    
    page.close()
