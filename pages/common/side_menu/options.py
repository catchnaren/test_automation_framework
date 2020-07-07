from pages.common.base_page import BasePage
from page.common.base_element import BaseElement
from selenium.webdriver.common.by import By
from pages.utils.locator import Locator


class Options(BasePage):

    @property
    def dashboard(self):
        locator = Locator(
            by=By.XPATH, value='//a[@id="lnkDashboardNavi"]/span[contains(text(), "Dashboard")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def workflows(self):
        locator = Locator(
            by=By.XPATH, value='//a[@id="lnkCFlowNavi"]/span[contains(text(), "Workflows")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def calendar(self):
        locator = Locator(
            by=By.XPATH, value='//a[@id="lnkCFlowCalenderNavi"]/span[contains(text(), "Calendar")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def reports(self):
        locator = Locator(
            by=By.XPATH, value='//a[@id="lnkReportNavi"]/span[contains(text(), "Reports")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def admin(self):
        locator = Locator(
            by=By.XPATH, value='//a[@id="lnkControlCenterNavi"]/span[contains(text(), "Admin")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def history(self):
        locator = Locator(
            by=By.XPATH, value='//a[@id="lnkHistoryNavi"]/span[contains(text(), "History")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def dashboard_designer(self):
        locator = Locator(
            by=By.XPATH, value='//a[@id="lnkDashboardConfigNavi"]/span[contains(text(), "Dashboard Designer")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_workflow(self):
        locator = Locator(
            by=By.XPATH, value='//span[@class="cf_navicontxt"][contains(text(), "Add Workflow")]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_lookup(self):
        locator = Locator(by=By.XPATH, value='')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def support(self):
        locator = Locator(by=By.XPATH, value='')
        return BaseElement(driver=self.driver, locator=locator)
