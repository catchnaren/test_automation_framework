from pages.common.base_page import BasePage
from pages.common.base_element import BaseElement
from selenium.webdriver.common.by import By
from pages.utils.locator import Locator


class LoginPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{self.base_url}login'

    @property
    def client_id_field(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#txtClientID')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def username_field(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#txtUserName')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_field(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#txtPassword')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_button(self):
        locator = Locator(
            by=By.XPATH, value='//a[@class="login-btn"][contains(text(), "Login")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def signup_link(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#sig-btn')
        return BaseElement(driver=self.driver, locator=locator)
