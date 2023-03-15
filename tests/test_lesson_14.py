from pytest_voluptuous import S
from schemas.schemas import *


def test_create_user(reqres):
    created_user = reqres.post("api/users", {"name": "Alex", "job": "Tester"})

    assert created_user.status_code == 201
    assert S(create_user) == created_user.json()
    assert created_user.json()["name"] == "Alex"
    assert created_user.json()["job"] == "Tester"


def test_update_user_by_put(reqres):
    update_user = reqres.put("api/users/2", {"name": "apopov", "job": "aqa"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "apopov"
    assert update_user.json()["job"] == "aqa"


def test_update_user_by_patch(reqres):
    update_user = reqres.put("api/users/2", {"name": "Popov", "job": "sdet"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "Popov"
    assert update_user.json()["job"] == "sdet"


def test_delete_user(reqres):
    delete_user = reqres.delete("api/users/2")

    assert delete_user.status_code == 204


def test_successful_register(reqres):
    user_register = reqres.post("api/register", {"email": "eve.holt@reqres.in", "password": "1234"})

    assert user_register.status_code == 200
    assert S(register_user) == user_register.json()
    assert user_register.json()['id']
    assert user_register.json()['token']


def test_unsuccessful_register(reqres):
    user_register = reqres.post("api/register", {"email": "5678@gmail.com"})

    assert user_register.status_code == 400
    assert S(unregister_user) == user_register.json()
    assert user_register.json()['error'] == 'Missing password'