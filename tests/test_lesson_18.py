import allure
from selene import have


def test_auth(app):
    app.open("")
    with allure.step('Check authentification'):
        app.element(".account").should(have.text("alexpo@gmail.com"))


def test_delete_product_from_wishlist(demoshop, app):
    app.open("")
    with allure.step('Add a product to wishlist'):
        demoshop.post("addproducttocart/details/14/2", json={"addtocart_14.EnteredQuantity": '1'})
    with allure.step('Delete a product from wishlist'):
        app.element('.ico-wishlist').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_delete_product_from_cart(demoshop, app):
    app.open("")
    with allure.step('Adding an item to the cart'):
        demoshop.post("addproducttocart/catalog/31/1/1")
    with allure.step('Checking if an item has been removed from the cart'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_delete_customer_address(demoshop, app):
    app.open("")
    with allure.step('Add address'):
        demoshop.post("customer/addressadd", json={"Address.Id": "0",
                                                   "Address.FirstName": "Alex",
                                                   "Address.LastName": "Popov",
                                                   "Address.Email": "alexpo@gmail.com",
                                                   "Address.Company": "Horns and hooves",
                                                   "Address.CountryId": "007",
                                                   "Address.StateProvinceId": "0",
                                                   "Address.City": "NY",
                                                   "Address.Address1": "baker street, 1",
                                                   "Address.Address2": "baker street, 2",
                                                   "Address.ZipPostalCode": "1231231",
                                                   "Address.PhoneNumber": "81111111111",
                                                   "Address.FaxNumber": "12321123"
                                                   })
    with allure.step('Checking delete address'):
        app.element('.account').click()
        app.element('.side-2 [href="/customer/addresses"]').click()
        app.element('.delete-address-button').click()
        app.driver.switch_to.alert.accept()
        app.element('.address-list').should(have.text('No addresses'))


def test_logout(app):
    app.open("")
    with allure.step('Check logout'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(have.text('Log in'))
