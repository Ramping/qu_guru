from selene.support.shared import browser
import os


def test_filling_form_personal_data():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Po')
    browser.element('#userEmail').type('alexpo@email.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('11111111111')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1991')
    browser.element('.react-datepicker__day--009').click()
    browser.element('#subjectsInput').type('math').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '5120x2160.png')
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('NY')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()
