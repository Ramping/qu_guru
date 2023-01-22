from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


def test_github():
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)


def test_dynamic_steps():
    with allure.step('Opening the main page'):
        browser.open('https://github.com')
    with allure.step('Looking for a repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()
    with allure.step('Go to repository link'):
        s(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Open the Issues tab'):
        s('#issues-tab').click()
    with allure.step('Checking for Issue number 76'):
        s(by.partial_text('#76')).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#76')


@allure.step('Opening the main page')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Looking for a repository')
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step('Go to repository link')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Open the Issues tab')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('Checking for Issue number 76')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
