from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage

def test_cart(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    product_page = ProductPage(page)
    product_page.add_to_cart()

    cart_page = CartPage(page)
    cart_page.navigate_to_cart()

    assert cart_page.is_cart_item_visible()
    page.close()
