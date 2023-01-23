from model.base_methods import _field_filling


def first_name(value):
    _field_filling('#firstName', value)


def second_name(value):
    _field_filling('#lastName', value)


def mail(value):
    _field_filling('#userEmail', value)
