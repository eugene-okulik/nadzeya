import requests

import pytest


@pytest.fixture
def new_object_id():
    body = {
        "data": {"color": "red", "size": "small"},
        "id": 1234,
        "name": "test object one"
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture
def individual():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='session')
def general():
    print('Start testing')
    yield
    print('Testing complete')


@pytest.mark.critical
def test_get_one_object(individual, general, new_object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}').json()
    assert response['id'] == new_object_id


def test_get_all_objects(individual):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200


@pytest.mark.medium
def test_put_an_object(individual, new_object_id):
    body = {
        "data": {"color": "green", "size": "medium"},
        "id": 1234,
        "name": "update test object one"
    }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body).json()
    assert response['data'] == {"color": "green", "size": "medium"}
    assert response['name'] == 'update test object one'


def test_patch_an_object(individual, new_object_id):
    body = {
        "name": "update2 test object one"
    }
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body).json()
    assert response['name'] == 'update2 test object one'


def test_delete_an_object(individual, new_object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200


@pytest.mark.parametrize('body, expected_status_code', [
    ({
        "data": {"color": "purple", "size": "small"},
        "id": 1241,
        "name": "test object1"}, 200),
    ({
        "data": {"color": "orange", "size": "small"},
        "id": 1242,
        "name": "test object2"}, 200),
    ({
        "data": {"color": "black", "size": "small"},
        "id": 1243,
        "name": "test object3"}, 200)])


def test_post_an_object(individual, body, expected_status_code):
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == expected_status_code
