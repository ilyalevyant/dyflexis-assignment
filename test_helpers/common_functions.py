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
    assert r.json()[
        "shortcode"], f"shortcode value is expected in response for create shorterner. Actual resoinse is {r.json()}"
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
    from config import Config
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
#
# @pytest.fixture
# def gists_data_factory():
#     from test_helpers.gists_data_factory import GistsDataFactory
#     gists_data_factory = GistsDataFactory()
#     return gists_data_factory
#
#
# @pytest.fixture
# def headers():
#     return {
#         'content-type': 'application/json',
#         'accept': 'application/vnd.github.v3+json',
#         'Authorization': 'token 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'
#     }
#
#
# @pytest.fixture
# def non_authorized_headers():
#     return {
#         'content-type': 'application/json',
#         'accept': 'application/vnd.github.v3+json'
#     }
#
#
# @pytest.fixture
# def gist(gists_test_helper, gists_data_factory):
#     """fixture to create gist, and delete it in test teardown"""
#     payload = gists_data_factory.create_gist_payload()
#     r = gists_test_helper.create_gist(payload)
#     assert r.status_code == 201, f"Status code for create gist is not as expected. Actual status code is {r.status_code}"
#     gist_id = r.json()['id']
#     yield gist_id
#     gists_test_helper.delete_gist_by_id(gist_id)
#
#
# @pytest.fixture
# def gists_conf():
#     from config import Config
#     config = Config()
#     return config
#
#
# @pytest.fixture
# def gists_test_helper(headers, gists_conf):
#     from test_helpers.gists_service_helper import GistsServiceHelper
#     gists_test_helper = GistsServiceHelper(headers, gists_conf)
#     return gists_test_helper
#
#
# @pytest.fixture
# def gists_test_helper_non_authorized(non_authorized_headers, gists_conf):
#     from test_helpers.gists_service_helper import GistsServiceHelper
#     gists_test_helper = GistsServiceHelper(non_authorized_headers, gists_conf)
#     return gists_test_helper
#
#
# def load_json_schema(filename: object) -> object:
#     """ Loads the given schemas file """
#     absolute_path = join(dirname(__file__), filename)
#     with open(absolute_path) as schema_file:
#         return json.loads(schema_file.read())
