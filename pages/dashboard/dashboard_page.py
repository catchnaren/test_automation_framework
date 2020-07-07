from pages.common.base_page import BasePage
from pages.common.base_element import BaseElement
from selenium.webdriver.common.by import By
from pages.utils.locator import Locator


class DashboardPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{self.base_url}dashboard-inbox'
        print(f'URL: {self.url}')

    @property
    def notifications(self):
        locator = Locator(
            by=By.XPATH, value='//span[@class="cf_sectiontitle"][contains(text(), "Notifications")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def my_workflows(self):
        locator = Locator(
            by=By.XPATH, value='//span[@class="cf_sectiontitle"][contains(text(), "My Workflows")]')
        return BaseElement(driver=self.driver, locator=locator)
