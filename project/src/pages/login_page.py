class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input_selector = "input#user-name"
        self.password_input_selector = "input#password"
        self.login_button_selector = "input.btn_action"
        self.title_selector = "span.title"
        self.error_message_selector = "h3[data-test='error']"
        self.expected_url = "https://www.saucedemo.com/inventory.html"

    def login(self, username, password):
        self.page.fill(self.username_input_selector, username)
        self.page.fill(self.password_input_selector, password)
        self.page.click(self.login_button_selector)

    def is_title_visible(self):
        return self.page.is_visible(self.title_selector)

    def get_title_text(self):
        return self.page.inner_text(self.title_selector)
    
    def get_error_message(self):
        return self.page.inner_text(self.error_message_selector)

    def is_logged_in(self):
        return self.page.url == self.expected_url