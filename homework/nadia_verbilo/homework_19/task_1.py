import requests


def new_object():
    body = {
        "data": {"color": "red", "size": "small"},
        "id": 1234,
        "name": "test object one"
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    return response.json()['id']


def clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def get_all_objects():
    requests.get('http://objapi.course.qa-practice.com/object').json()


def get_one_object():
    object_id = new_object()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}').json()
    assert response['id'] == object_id, 'Error returning one object'


def post_an_object():
    body = {
        "data": {"color": "black", "size": "big"},
        "id": 4321,
        "name": "test object two"
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200, 'Status code is not correct'


def put_an_object():
    object_id = new_object()
    body = {
        "data": {"color": "green", "size": "medium"},
        "id": 12345,
        "name": "update test object one"
    }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body).json()
    assert response['data'] == {"color": "green", "size": "medium"}, 'Error in data update'
    assert response['id'] == 12345, 'Error in id update'
    assert response['name'] == 'update test object one', 'Error in name update'
    clear(object_id)


def patch_an_object():
    object_id = new_object()
    body = {
        "id": 12345
    }
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body).json()
    assert response['id'] == 12345, 'Error in id update'
    clear(object_id)


def delete_an_object():
    object_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}').json()
    print(response.status_code)
    assert response.status_code == 200, 'Status code is not correct'


get_all_objects()
get_one_object()
post_an_object()
put_an_object()
patch_an_object()
delete_an_object()
