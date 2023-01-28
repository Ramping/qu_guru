from selene import have
from selene.support.shared import browser


def element(locator):
    return browser.element(locator)


def field_filling(locator, value):
    element(locator).type(value)


def click_on_element(locator):
    element(locator).click()


def selection_from_list(locator, value):
    element(locator).type(value).press_enter()


def send_key(locator, value):
    element(locator).send_keys(value)


def checking_elements(selector, *value):
    browser.all(selector).should(have.texts(*value))
