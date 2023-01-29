from demoqa_tests.base_methods import element


def dropdown(locator, value):
    element(locator).type(value).press_enter()
