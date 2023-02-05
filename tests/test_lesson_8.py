import pytest
from selene.support.shared import browser
from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.student import Student, Hobby, Gender


@pytest.mark.parametrize('url', ['automation-practice-form'])
def test_filling_form_personal_data(url):
    pf = PracticePage()
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
    browser.open(url)
    pf.first_name(student_alex).last_name(student_alex).email(student_alex).gender(student_alex)\
        .phone(student_alex).birthday(student_alex).subjects(student_alex).hobbies(student_alex)\
        .address(student_alex).country(student_alex).city(student_alex).insert_image(student_alex).submit()
    pf.check_end_form(
        f'{student_alex.first_name} {student_alex.last_name}',
        student_alex.email,
        student_alex.gender.name,
        student_alex.phone,
        f'{student_alex.birthday[0]} {student_alex.birthday[1]},{student_alex.birthday[2]}',
        student_alex.subject,
        student_alex.hobby[0].name,
        student_alex.image,
        student_alex.address,
        f'{student_alex.state} {student_alex.city}'
    )
