import jsonschema
import requests

from utils.utils import load_schema

BASE_URL = "https://reqres.in"


def test_single_user_succsessfully():
    url = f"{BASE_URL}/api/users/2"
    schema = load_schema("../utils/schema/get_single_user.json")

    results = requests.get(url)

    assert results.status_code == 200
    jsonschema.validate(results.json(), schema)
    assert results.json()["data"]["id"] == 2
    assert results.json()["data"]["first_name"] == "Janet"
    assert results.json()["data"]["last_name"] == "Weaver"
    assert results.json()["data"]["email"] == "janet.weaver@reqres.in"


def test_create_user_succseddfully():
    url = f"{BASE_URL}/api/users/"
    schema = load_schema("../utils/schema/create_user.json")
    body = {
        "name": "aleksey",
        "job": "student"
    }

    results = requests.post(url, body)

    assert results.status_code == 201
    jsonschema.validate(results.json(), schema)
    assert results.json()["name"] == "aleksey"
    assert results.json()["job"] == "student"


def test_update_user_succseddfully():
    id_update_user = 2
    url = f"{BASE_URL}/api/users/{id}"
    schema = load_schema("../utils/schema/update_user.json")
    body = {
        "name": "aleksey_petrov",
        "job": "student"
    }

    results = requests.put(url, body)

    assert results.status_code == 200
    jsonschema.validate(results.json(), schema)
    assert results.json()["name"] == "aleksey_petrov"
    assert results.json()["job"] == "student"


def test_delete_user_succseddfully():
    id_update_user = 2
    url = f"{BASE_URL}/api/users/{id}"

    results = requests.delete(url)

    assert results.status_code == 204


def test_register_user_succseddfully():
    url = f"{BASE_URL}/api/register"
    schema = load_schema("../utils/schema/register_user.json")
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    results = requests.post(url, body)

    assert results.status_code == 200
    jsonschema.validate(results.json(), schema)


def test_login_user_succseddfully():
    url = f"{BASE_URL}/api/register"
    schema = load_schema("../utils/schema/login_user.json")
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    results = requests.post(url, body)

    assert results.status_code == 200
    jsonschema.validate(results.json(), schema)


def test_single_user_unsuccseddfully():
    url = f"{BASE_URL}/api/users/23"
    schema = load_schema("../utils/schema/get_single_user.json")

    results = requests.get(url)

    assert results.status_code == 404


def test_register_user_unsuccseddfully():
    url = f"{BASE_URL}/api/register"
    body = {
        "email": "eve.holt@reqres.in",
        "password": ""
    }

    results = requests.post(url, body)

    assert results.status_code == 400
    assert results.json() == {
        "error": "Missing password"
    }


def test_login_user_unsuccseddfully():
    url = f"{BASE_URL}/api/register"
    body = {
        "email": "eve.holt@reqres.in",
        "password": ""
    }

    results = requests.post(url, body)

    assert results.status_code == 400
    assert results.json() == {
        "error": "Missing password"
    }
