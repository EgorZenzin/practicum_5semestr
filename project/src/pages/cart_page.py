class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_link_selector = "a.shopping_cart_link"
        self.cart_item_selector = "div.cart_item"

    def navigate_to_cart(self):
        self.page.click(self.cart_link_selector)

    def is_cart_item_visible(self):
        return self.page.is_visible(self.cart_item_selector)
