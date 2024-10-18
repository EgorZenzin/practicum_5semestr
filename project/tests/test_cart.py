from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

def test_cart(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("input#user-name", "standard_user")
    page.fill("input#password", "secret_sauce")
    page.click("input.btn_action")
    
    product_page = ProductPage(page)
    product_page.add_to_cart()

    cart_page = CartPage(page)
    cart_page.navigate_to_cart()

    assert page.is_visible("div.cart_item")
    page.close()
