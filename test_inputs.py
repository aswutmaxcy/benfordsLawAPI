from userdata import UserData
from respmodel import BenfordResponse

data = UserData(data=[1, 2, 3, 4])

bad_data = [1, 2, 2, 3]

resp_model = BenfordResponse(
    P=5.1,
    t=2.3,
    prediction=True,
    percentage_matrix=[
        [1.0, 24.0],
        [2.0, 20.0],
        [3.0, 12.0],
        [4.0, 8.0],
        [5.0, 8.0],
        [6.0, 4.0],
        [7.0, 8.0],
        [8.0, 8.0],
        [9.0, 8.0],
    ],
)


def test_is_UserData():
    assert type(data) is UserData


def test_is_data_list():
    assert type(data.data) is list


def test_are_data_items_ints():
    for item in data.data:
        assert type(item) is int


def test_bad_data():
    assert type(bad_data) is not UserData
    for item in bad_data:
        assert type(item) is int


def test_resp_is_BenfordResponse():
    assert type(resp_model) is BenfordResponse
    assert type(resp_model.percentage_matrix[0]) is list
    assert type(resp_model.percentage_matrix[0][1]) is float

    for item in resp_model.percentage_matrix:
        assert type(item) is list
        print(type(item))
        print(item)