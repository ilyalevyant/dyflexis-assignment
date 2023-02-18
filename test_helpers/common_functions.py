import uuid
from http import HTTPStatus
from os.path import join, dirname
import json
import pytest
import requests

from test_helpers.config import Config

def create_query_by_params(parameters):
    result = "?"
    for field_name, field_value in parameters:
        result = result + f"{field_name}={field_value}&"
    return result


@pytest.fixture
def rnd_value():
    return str(uuid.uuid1())[0:6]


@pytest.fixture
def booking_id(booking_service, rnd_value, booking_data_factory):
    payload = booking_data_factory.create_booking_payload(rnd_value)
    r = booking_service.create_booking(payload=payload)
    assert r.status_code == HTTPStatus.OK, f"status code for create booking is {r.status_code}"
    return r.json()["bookingid"]


def load_json_schema(filename: object) -> object:
    """ Loads the given schemas file """
    absolute_path = join(dirname(__file__), filename)
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
