from selene.support.shared import browser


def _field_filling(locator, value):
    browser.element(locator).type(value)
