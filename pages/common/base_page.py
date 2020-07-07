class BasePage(object):

    url = None

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def go(self):
        self.driver.get(self.url)
