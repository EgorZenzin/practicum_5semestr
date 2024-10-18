def test_display(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("input#user-name", "standard_user")
    page.fill("input#password", "secret_sauce")
    page.click("input.btn_action")

    assert page.is_visible("span.title") 
    assert page.inner_text("span.title") == "Products"  
    page.close()
