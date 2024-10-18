class CartPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_cart(self):
        self.page.click("a.shopping_cart_link")
