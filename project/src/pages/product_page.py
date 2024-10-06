class ProductPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, product_index):
        self.page.click(f"button[data-test='add-to-cart-sauce-labs-backpack']")  # Пример для первого продукта

    def go_to_cart(self):
        self.page.click("a.shopping_cart_link")
