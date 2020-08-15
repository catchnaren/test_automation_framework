from pages.common.base_page import BasePage
from pages.common.base_element import BaseElement
from selenium.webdriver.common.by import By
from pages.utils.locator import Locator


class SignupPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{self.base_url}signup'

    @property
    def signup_email_field(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#txtEmail')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def check_box(self):
        locator = Locator(
            by=By.XPATH, value='//label[contains(text(), "I Agree")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def start_free_trial_button(self):
        locator = Locator(
            by=By.XPATH, value='//a[@class="login-btn"][contains(text(), "Start Free Trial")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def success_message(self):
        locator = Locator(
            by=By.XPATH, value='//div[@class="message-ico isuccess"]/span')
        return BaseElement(driver=self.driver, locator=locator)
