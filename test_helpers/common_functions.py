import uuid
from http import HTTPStatus
from os.path import join, dirname
import json
import pytest


@pytest.fixture
def headers():
    return {
        'content-type': 'application/json'
    }


@pytest.fixture
def rnd_url():
    return str(uuid.uuid1())[0:16]


@pytest.fixture
def rnd_shortcode():
    return str(uuid.uuid1())[0:6]


@pytest.fixture
def created_shortcode(shorterner_service, rnd_url, shorterner_data_factory):
    payload = shorterner_data_factory.create_shorterner_payload(rnd_url)
    r = shorterner_service.create_shortcode(payload)
    assert r.status_code == HTTPStatus.CREATED, f"status code for create shorterner is {r.status_code}"
    assert len(r.json()["shortcode"]) == 6, f"shortcode value is not as expected in response for create shorterner. Actual resoinse is {r.json()}"
    return r.json()["shortcode"]


@pytest.fixture
def created_shortcode_with_specific_code(shorterner_service, rnd_url, rnd_shortcode, shorterner_data_factory):
    payload = shorterner_data_factory.create_shorterner_payload(rnd_url, rnd_shortcode)
    r = shorterner_service.create_shortcode(payload)
    assert r.status_code == HTTPStatus.CREATED, f"status code for create shorterner is {r.status_code}"
    assert r.json()["shortcode"] == rnd_shortcode, f"shortcode value in response is not equals to provided value. Actual resoinse is {r.json()}"
    return r.json()["shortcode"]


@pytest.fixture
def shorterner_conf():
    from test_helpers.config import Config
    config = Config()
    return config


@pytest.fixture
def shorterner_service(headers, shorterner_conf):
    from test_helpers.shorterner_service_helper import ShorternerService
    return ShorternerService(headers, shorterner_conf)


@pytest.fixture
def shorterner_data_factory():
    from test_helpers.shorterner_data_factory import ShorternerDataFactory
    return ShorternerDataFactory()


def load_json_schema(filename: object) -> object:
    """ Loads the given schemas file """
    absolute_path = join(dirname(__file__), filename)
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
