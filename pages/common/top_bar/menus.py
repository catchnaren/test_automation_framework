from pages.common.base_page import BasePage
from page.common.base_element import BaseElement
from selenium.webdriver.common.by import By
from pages.utils.locator import Locator


class Menus(BasePage):

    @property
    def upload_logo(self):
        locator = Locator(by=By.CSS_SELECTOR, value='img#imgClientLogo')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def help_icon(self):
        locator = Locator(by=By.CSS_SELECTOR, value='i.icon-help-circle')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def profile_options_dropdown(self):
        locator = Locator(
            by=By.XPATH, value='//a[@class="icon_gap_a dropdown-toggle"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def profile(self):
        locator = Locator(
            by=By.XPATH, value='//a[@class="icon_text_gap_a"]/span[contains(text(), "Profile")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def logout(self):
        locator = Locator(
            by=By.XPATH, value='//a[@class="icon_text_gap_a FnLogout"]/span')
        return BaseElement(driver=self.driver, locator=locator)
