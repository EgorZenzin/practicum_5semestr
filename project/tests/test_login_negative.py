import pytest
from playwright.sync_api import sync_playwright
from src.pages.login_page import LoginPage

def test_login_with_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("invalid_user", "invalid_password")

        assert login_page.is_error_visible(), "Сообщение об ошибке не отображается."

        context.close()
        browser.close()
