from demoqa_tests.base_methods import field_filling, click_on_element, send_key, element, checking_elements
from demoqa_tests.model.controls.dropdown import dropdown
from demoqa_tests.model.controls.datepicker import datepicker
from demoqa_tests.utils.path_generator import images


def first_name(value):
    field_filling('#firstName', value)


def second_name(value):
    field_filling('#lastName', value)


def mail(value):
    field_filling('#userEmail', value)


def gender():
    click_on_element('[for=gender-radio-1]')


def number(value):
    field_filling('#userNumber', value)


def subjects(value):
    dropdown('#subjectsInput', value)


def birthday(month, year):
    datepicker(
        '#dateOfBirthInput',
        '.react-datepicker__month-select',
        '.react-datepicker__year-select',
        '.react-datepicker__day--009',
        month,
        year
    )


def hobbies():
    click_on_element('[for=hobbies-checkbox-1]')


def insert_image(file_name):
    send_key('#uploadPicture', images(file_name))


def address(value):
    field_filling('#currentAddress', value)


def country(value):
    dropdown('#react-select-3-input', value)


def city(value):
    dropdown('#react-select-4-input', value)


def submit():
    element('#submit').press_enter()


def check_end_form(*value):
    checking_elements('.table-responsive td:nth-child(2)', *value)
