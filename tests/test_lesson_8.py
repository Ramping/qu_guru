import pytest
from selene import have
from selene.support.shared import browser
import os
from model import practice_form as pf


@pytest.mark.parametrize('url', ['automation-practice-form'])
def test_filling_form_personal_data(url):
    browser.open(url)
    pf.first_name('Alex')
    pf.second_name('Po')
    pf.mail('alexpo@email.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('11111111111')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1991')
    browser.element('.react-datepicker__day--009').click()
    browser.element('#subjectsInput').type('math').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(os.path.join('resources', 'icons8-laptop-96.png')))
    browser.element('#currentAddress').type('NY')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Alex Po',
        'alexpo@email.com',
        'Male',
        '1111111111',
        '09 October,1991',
        'Maths',
        'Sports',
        'icons8-laptop-96.png',
        'NY',
        'NCR Delhi'
    )
    )
