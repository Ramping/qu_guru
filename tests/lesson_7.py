from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'popov')
@allure.feature('Tasks in the repository')
@allure.story('Sample test without steps')
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('Ramping/qu_guru')
    s('.header-search-input').submit()

    s(by.link_text('Ramping/qu_guru')).click()

    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'popov')
@allure.feature('Tasks in the repository')
@allure.story('Sample test with lambda steps')
@allure.link('https://github.com', name='Testing')
def test_dynamic_steps():
    with allure.step('Opening the main page'):
        browser.open('https://github.com')
    with allure.step('Looking for a repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('Ramping/qu_guru')
        s('.header-search-input').submit()
    with allure.step('Go to repository link'):
        s(by.link_text('Ramping/qu_guru')).click()
    with allure.step('Open the Issues tab'):
        s('#issues-tab').click()
    with allure.step('Checking for Issue number 1'):
        s(by.partial_text('#1')).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'popov')
@allure.feature('Tasks in the repository')
@allure.story('Decorator test example')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository('Ramping/qu_guru')
    go_to_repository('Ramping/qu_guru')
    open_issue_tab()
    should_see_issue_with_number('#1')


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


@allure.step('Checking for Issue number 1')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
