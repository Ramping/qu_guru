from demoqa_tests.base_methods import BaseMethods

bf = BaseMethods()


def dropdown(locator, value):
    bf.element(locator).type(value).press_enter()
