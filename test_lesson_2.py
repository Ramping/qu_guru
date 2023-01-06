import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def browser_config():
    browser.config.window_width = 800
    browser.config.window_height = 600
    browser.config.hold_browser_open = True


def test_open_browser(browser_config):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type('selene framework').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative(browser_config):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type('ahuegfuyegf87f').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
