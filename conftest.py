from http import HTTPStatus

import pytest
import requests

from test_helpers.config import Config


def pytest_addoption(parser):
    parser.addoption("--username", action="store", default="default")
    parser.addoption("--password", action="store", default="default")


@pytest.fixture
def headers():
    return {
        'Content-type': 'application/json'
    }


@pytest.fixture
def auth_headers(pytestconfig):
    r = requests.post(Config.auth_endpoint, json={"username": pytestconfig.getoption("username"), "password": pytestconfig.getoption("password")})
    assert r.status_code == HTTPStatus.OK, f'Token was not created successfully. {r.text}'
    token = r.json()['token']
    return {
        'Content-type': 'application/json',
        'Cookie': f'token={token}'
    }


@pytest.fixture
def booking_conf():
    from test_helpers.config import Config
    config = Config()
    return config


@pytest.fixture
def auth_booking_service(auth_headers, booking_conf):
    from test_helpers.booking_service_helper import BookingService
    return BookingService(auth_headers, booking_conf)


@pytest.fixture
def booking_data_factory():
    from test_helpers.booking_data_factory import BookingDataFactory
    return BookingDataFactory()


@pytest.fixture
def booking_service(headers, booking_conf):
    from test_helpers.booking_service_helper import BookingService
    return BookingService(headers, booking_conf)



