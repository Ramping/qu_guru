import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('browser_open', ["900x940"], indirect=True)
def test_mobile_indirect(browser_open):
    browser.element('.js-details-target.Button--link').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('browser_open', ["1920x1080"], indirect=True)
def test_desktop_indirect(browser_open):
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('width, height', [pytest.param(1920, 1080, id='1920x1080'),
                                           pytest.param(900, 940, id='900x940')
                                           ])
def test_desktop(browser_chrome, width, height):
    if width == 900:
        pytest.skip("Desktop")
    browser.driver.set_window_size(width, height)
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('width, height', [pytest.param(1920, 1080, id='1920x1080'),
                                           pytest.param(900, 940, id='900x940')
                                           ])
def test_mobile(browser_chrome, width, height):
    if width == 1920:
        pytest.skip("Mobile")
    browser.driver.set_window_size(width, height)
    browser.element('.js-details-target.Button--link').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
