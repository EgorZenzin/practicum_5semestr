class ProductPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button_selector = "button.btn_primary"

    def add_to_cart(self):
        self.page.click(self.add_to_cart_button_selector)
