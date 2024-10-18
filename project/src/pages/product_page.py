class ProductPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        self.page.click("button.btn_primary")
