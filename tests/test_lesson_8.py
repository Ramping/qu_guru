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
    pf.gender()
    pf.number('11111111111')
    pf.birthday('October', '1991')
    pf.subjects('math')
    pf.hobbies()
    pf.insert_image('icons8-laptop-96.png')
    pf.address('NY')
    pf.country('NCR')
    pf.city('Delhi')
    pf.submit()
    pf.check_end_form(
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
