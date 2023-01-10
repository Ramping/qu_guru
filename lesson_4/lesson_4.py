def new_func_name(def_name, *args):
    def_name = def_name.__name__.title().replace('_', ' ')
    arg_func = ', '.join(list(args))
    print(f'Function name: {def_name}. Function arguments: {arg_func}')


def open_browser(browser_name):
    return new_func_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    return new_func_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    return new_func_name(find_registration_button_on_login_page, page_url, button_text)


if __name__ == '__main__':
    open_browser('Chrome')
    go_to_companyname_homepage('https://tesla.com')
    find_registration_button_on_login_page('https://mercedes.com', 'Buy now')
