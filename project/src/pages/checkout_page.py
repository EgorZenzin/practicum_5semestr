class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill("input#first-name", first_name)
        self.page.fill("input#last-name", last_name)
        self.page.fill("input#postal-code", postal_code)
        self.page.click("input#continue")

    def is_checkout_complete(self):
        return self.page.url == "https://www.saucedemo.com/checkout-complete.html"
