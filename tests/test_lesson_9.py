import allure
import pytest
from selene.support.shared import browser
from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.student import Student, Hobby, Gender


@pytest.mark.parametrize('url', ['automation-practice-form'])
def test_filling_form_personal_data(url):
    pp = PracticePage()
    student_alex = Student(
        first_name='Alex',
        last_name='Po',
        email='alexpo@email.com',
        phone='1111111111',
        gender=Gender.Male,
        birthday=['09', 'October', '1991'],
        subject='Maths',
        hobby=[Hobby.Sports],
        image='icons8-laptop-96.png',
        address='NY',
        state='NCR',
        city='Delhi'
    )
    with allure.step('Open registration form'):
        browser.open(url)
    with allure.step('Fill registration form'):
        pp.fill(student_alex)
    with allure.step('Check results registration form'):
        pp.check_results(student_alex)
