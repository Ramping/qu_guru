from demoqa_tests.base_methods import click_on_element, field_filling


def datepicker(locator_calendar, locator_month, locator_year, locator_day, month, year):
    click_on_element(locator_calendar)
    field_filling(locator_month, month)
    field_filling(locator_year, year)
    click_on_element(locator_day)
