from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

    def click_by_offset(self, x, y):
        action = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        location = element.location
        print(f'ELEMENT LOCATION: {location}')
        action.move_to_element_with_offset(
            element, x, y).click().perform()
        return None
