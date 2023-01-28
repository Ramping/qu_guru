from collections.abc import Iterable

from model.base_methods import field_filling, click_on_element, selection_from_list, send_key, element, checking_elements
from model.path_generator import images


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


def birthday(month, year):
    click_on_element('#dateOfBirthInput')
    field_filling('.react-datepicker__month-select', month)
    field_filling('.react-datepicker__year-select', year)
    click_on_element('.react-datepicker__day--009')


def subjects(value):
    selection_from_list('#subjectsInput', value)


def hobbies():
    click_on_element('[for=hobbies-checkbox-1]')


def insert_image(file_name):
    send_key('#uploadPicture', images(file_name))


def address(value):
    field_filling('#currentAddress', value)


def country(value):
    selection_from_list('#react-select-3-input', value)


def city(value):
    selection_from_list('#react-select-4-input', value)


def submit():
    element('#submit').press_enter()


def check_end_form(*value):
    checking_elements('.table-responsive td:nth-child(2)', *value)
