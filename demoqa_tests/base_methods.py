from selene import have
from selene.support.shared import browser


class BaseMethods:

    def __init__(self):
        self.browser = browser

    def element(self, locator):
        return self.browser.element(locator)

    def field_filling(self, locator, value):
        self.element(locator).type(value)

    def click_on_element(self, locator):
        self.element(locator).click()

    def send_key(self, locator, value):
        self.element(locator).send_keys(value)

    def checking_elements(self, selector, *value):
        self.browser.all(selector).should(have.texts(*value))
