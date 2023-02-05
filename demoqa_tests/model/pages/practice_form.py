from demoqa_tests.base_methods import BaseMethods
from demoqa_tests.model.controls.dropdown import dropdown
from demoqa_tests.model.controls.datepicker import datepicker
from demoqa_tests.utils.path_generator import images


class PracticePage:
    def __init__(self):
        self.bf = BaseMethods()

    def first_name(self, student):
        self.bf.field_filling('#firstName', student.first_name)
        return self

    def last_name(self, student):
        self.bf.field_filling('#lastName', student.last_name)
        return self

    def email(self, student):
        self.bf.field_filling('#userEmail', student.email)
        return self

    def gender(self, student):
        self.bf.click_on_element(f'[for=gender-radio-{student.gender.value[0]}]')
        return self

    def phone(self, student):
        self.bf.field_filling('#userNumber', student.phone)
        return self

    def subjects(self, student):
        dropdown('#subjectsInput', student.subject)
        return self

    def birthday(self, student):
        datepicker(
            '#dateOfBirthInput',
            '.react-datepicker__month-select',
            '.react-datepicker__year-select',
            f'.react-datepicker__day--0{student.birthday[0]}',
            student.birthday[1],
            student.birthday[2]
        )
        return self

    def hobbies(self, student):
        self.bf.click_on_element(f'[for=hobbies-checkbox-{student.hobby[0].value[0]}]')
        return self

    def insert_image(self, student):
        self.bf.send_key('#uploadPicture', images(student.image))
        return self

    def address(self, student):
        self.bf.field_filling('#currentAddress', student.address)
        return self

    def country(self, student):
        dropdown('#react-select-3-input', student.state)
        return self

    def city(self, student):
        dropdown('#react-select-4-input', student.city)
        return self

    def submit(self):
        self.bf.element('#submit').press_enter()
        return self

    def check_end_form(self, *value):
        self.bf.checking_elements('.table-responsive td:nth-child(2)', *value)
        return self
