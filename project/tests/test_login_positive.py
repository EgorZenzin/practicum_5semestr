import pytest
from playwright.sync_api import sync_playwright
from src.pages.login_page import LoginPage

def test_login_with_valid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert page.url == "https://www.saucedemo.com/inventory.html", "Пользователь не был перенаправлен на страницу каталога."

        context.close()
        browser.close()
