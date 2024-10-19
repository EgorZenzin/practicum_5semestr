class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button_selector = "button.btn_action.checkout_button"  

    def checkout(self):
        self.page.click(self.checkout_button_selector)  
