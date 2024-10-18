class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.click("button[class='btn_action checkout_button']")
