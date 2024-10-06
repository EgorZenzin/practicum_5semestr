class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill("input#user-name", username)
        self.page.fill("input#password", password)
        self.page.click("input#login-button")

    def is_error_visible(self):
        return self.page.is_visible("h3[data-test='error']")
