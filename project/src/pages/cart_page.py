from src.pages.checkout_page import CheckoutPage

class CartPage:
    def __init__(self, page):
        self.page = page

    def is_cart_not_empty(self):
        return len(self.page.query_selector_all(".cart_item")) > 0

    def finish_checkout(self):
        self.page.click("button.checkout")
        return CheckoutPage(self.page)
