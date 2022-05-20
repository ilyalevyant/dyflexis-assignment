from os.path import join, dirname
import json
import pytest


@pytest.fixture
def gists_data_factory():
    from test_helpers.gists_data_factory import GistsDataFactory
    gists_data_factory = GistsDataFactory()
    return gists_data_factory


@pytest.fixture
def headers():
    return {
        'content-type': 'application/json',
        'accept': 'application/vnd.github.v3+json',
        'Authorization': 'token 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'
    }


@pytest.fixture
def non_authorized_headers():
    return {
        'content-type': 'application/json',
        'accept': 'application/vnd.github.v3+json'
    }


@pytest.fixture
def gist(gists_test_helper, gists_data_factory):
    """fixture to create gist, and delete it in test teardown"""
    payload = gists_data_factory.create_gist_payload()
    r = gists_test_helper.create_gist(payload)
    assert r.status_code == 201, f"Status code for create gist is not as expected. Actual status code is {r.status_code}"
    gist_id = r.json()['id']
    yield gist_id
    gists_test_helper.delete_gist_by_id(gist_id)


@pytest.fixture
def gists_conf():
    from config import Config
    config = Config()
    return config


@pytest.fixture
def gists_test_helper(headers, gists_conf):
    from test_helpers.gists_service_helper import GistsServiceHelper
    gists_test_helper = GistsServiceHelper(headers, gists_conf)
    return gists_test_helper


@pytest.fixture
def gists_test_helper_non_authorized(non_authorized_headers, gists_conf):
    from test_helpers.gists_service_helper import GistsServiceHelper
    gists_test_helper = GistsServiceHelper(non_authorized_headers, gists_conf)
    return gists_test_helper


def load_json_schema(filename: object) -> object:
    """ Loads the given schemas file """
    absolute_path = join(dirname(__file__), filename)
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
