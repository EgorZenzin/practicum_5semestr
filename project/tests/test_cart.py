import pytest
from playwright.sync_api import sync_playwright
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

def test_add_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        product_page = ProductPage(page)
        product_page.add_to_cart(1)

        product_page.go_to_cart()
        cart_page = CartPage(page)

        assert cart_page.is_cart_not_empty(), "Корзина должна содержать хотя бы один товар."

        context.close()
        browser.close()
