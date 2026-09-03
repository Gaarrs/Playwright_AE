from playwright.sync_api import Page, expect
from urllib3.util import timeout


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = page.url
        self.logo = page.get_by_alt_text("Website for automation practice")
        self.home_link = page.locator("a:text(' Home')")
        self.products_link = page.locator("a:text(' Products')")
        self.cart_link = page.locator("a:text(' Cart')")
        self.login_link = page.locator("a:text(' Signup / Login')")
        self.tests_link = page.locator("a:text(' Test Cases')")
        self.api_link = page.locator("a:text(' API Testing')")
        self.contact_link = page.locator("a:text(' Contact Us')")
        self.logout_link = page.locator("a:text(' Logout')")
        self.delete_acc_link = page.locator("a:text(' Delete Account')")
        self.logged_status = page.locator("a:text('Logged')")
        self.sub_input = page.get_by_placeholder("Your email address")
        self.sub_button = page.locator("#subscribe")
        self.scroll_button = page.locator("#scrollUp")
        self.subscription_text = page.locator("h2:text('Subscription')")

    def navigate(self, url: str):
        self.page.goto(url, timeout=60000)

    def open_cart(self):
        self.cart_link.click()

    def subscribe(self, email: str):
        self.sub_input.fill(email)
        self.sub_button.click()

    def scroll_up(self):
        self.scroll_button.click()