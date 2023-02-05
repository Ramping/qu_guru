from demoqa_tests.base_methods import BaseMethods

bf = BaseMethods()


def datepicker(locator_calendar, locator_month, locator_year, locator_day, month, year):
    bf.click_on_element(locator_calendar)
    bf.field_filling(locator_month, month)
    bf.field_filling(locator_year, year)
    bf.click_on_element(locator_day)
