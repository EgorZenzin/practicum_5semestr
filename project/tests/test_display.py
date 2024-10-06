import pytest
from playwright.sync_api import sync_playwright
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage

def test_display_products():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        product_page = ProductPage(page)

        products = page.query_selector_all(".inventory_item")
        assert len(products) > 0, "Не отображается ни один продукт."

        for product in products:
            product_name = product.query_selector(".inventory_item_name")
            product_price = product.query_selector(".inventory_item_price")
            assert product_name and product_name.inner_text() != "", "Название продукта не должно быть пустым."
            assert product_price and product_price.inner_text() != "", "Цена продукта не должна быть пустой."

        context.close()
        browser.close()
