from test_helpers.common_functions import *


def test_create_gist(gists_test_helper, gists_data_factory):
    """
    1. Create new gist
    2. Validate status code is 201.
    3. Validate response body as expected.
    4. Validate with get API that gist was saved in DB as expected
    """
    payload = gists_data_factory.create_gist_payload()
    r = gists_test_helper.create_gist(payload)
    assert r.status_code == 201, f"Status code for create gist is not as expected. Actual status code is {r.status_code}"
    expected_result = gists_data_factory.create_gist_expected_result()
    create_gist_response = r.json()
    actual_result = gists_data_factory.actual_result_create_gist(r.json())
    assert actual_result == expected_result, f"Response body is not as expected for create gist. Actual response is {create_gist_response}"

    gist_id = r.json()['id']
    r = gists_test_helper.get_gist_by_id(gist_id)
    assert r.status_code == 200, f'Status code for get gist by id is not as expected. Actual status code is {r.status_code}'
    assert r.json() == create_gist_response, 'Response for get gist is not equals to response for create gist'


@pytest.mark.parametrize('params', [('description', None), ('public', False)])
def test_create_gist_mandatory_fields_only(gists_test_helper, gists_data_factory, params):
    """
    1. Create new gist without each of mandatory field.
    2. Validate status code is 201.
    3. Validate response body as expected.
    4. Validate with get API that gist was saved in DB as expected.
    5. Validate default value for non-mandatory field.
    """
    field, default_value = params
    payload = gists_data_factory.create_gist_payload()
    del(payload[field])

    r = gists_test_helper.create_gist(payload)
    assert r.status_code == 201, f"Status code for create gist without {field} is wrong. Actual status code is {r.status_code}"
    expected_result = gists_data_factory.create_gist_expected_result(non_mandatory_filed=params)
    create_gist_response = r.json()
    assert create_gist_response['updated_at']
    del(create_gist_response['updated_at'])

    actual_result = gists_data_factory.actual_result_create_gist(r.json())
    assert actual_result == expected_result, f"Response body is not as expected for create gist. Actual response is {create_gist_response}"
    gist_id = r.json()['id']
    r = gists_test_helper.get_gist_by_id(gist_id)
    assert r.status_code == 200, f'Status code for get gist by id is not as expected. Actual status code is {r.status_code}'
    actual_result = r.json()
    assert actual_result['updated_at']
    del(actual_result['updated_at'])
    assert actual_result == create_gist_response, 'Response for get gist is not equals to response for create gist'


def test_create_gist_no_token_negative(gists_test_helper_non_authorized, gists_data_factory):
    """
    1. Try to create new gist without token
    2. Validate an error.
    """
    payload = gists_data_factory.create_gist_payload()
    r = gists_test_helper_non_authorized.create_gist(payload)
    assert r.status_code == 401, f"Status code for create gist is not as expected. Actual status code is {r.status_code}"
    assert r.json() == {"message":"Requires authentication","documentation_url":"https://docs.github.com/rest/reference/gists#create-a-gist"}, \
        "error is not as expected for non authorized request"


def test_create_gists_without_files_negative(gists_test_helper, gists_data_factory):
    """
    1. Try to create new gist without files in request
    2. Validate an error.
    """
    r = gists_test_helper.create_gist({})
    assert r.status_code == 422, f"Status code for create gist is not as expected. Actual status code is {r.status_code}"


def test_update_gist(gists_test_helper, gists_data_factory, gist):
    """
    1. Create gist.
    2. Update all fields by patch.
    3. Get gist by id and validate 'files' and 'description' were updated successfully.
    """
    create_gist_payload = gists_data_factory.create_gist_payload()
    update_gist_payload = gists_data_factory.update_gist_payload()
    r = gists_test_helper.update_gist_by_id(update_gist_payload, gist)
    assert r.status_code == 200, f'Status code for get gist by id is not as expected. Actual status code is {r.status_code}'
    r = gists_test_helper.get_gist_by_id(gist)
    updated_gist = r.json()
    assert updated_gist['files']['some_test_file']['content'] == create_gist_payload['files']['some_test_file']['content'], \
        'existing file was replaced by patch request'
    assert updated_gist['files']['update_file_name']['content'] == update_gist_payload['files']['update_file_name']['content'], \
        'new file was not added by patch request'
    assert updated_gist['description'] == update_gist_payload['description'], 'description was not updated in gist by patch'


def test_update_gist_without_token_negative(gists_test_helper_non_authorized, gists_data_factory, gist):
    """
    1. Create gist.
    2. Try to update it without token.
    3. Validate an error.
    """
    r = gists_test_helper_non_authorized.update_gist_by_id({}, gist)
    assert r.status_code == 404, f'Status code for get gist by id is not as expected. Actual status code is {r.status_code}'


def test_update_non_existin_gist_negative(gists_test_helper, gists_data_factory):
    """
    1. Try to update non-existing gist.
    2. Validate an error.
    """
    update_gist_payload = gists_data_factory.update_gist_payload()
    r = gists_test_helper.update_gist_by_id(update_gist_payload, 'invalid_id')
    assert r.status_code == 404, f'Status code for update gist by invalid id is not as expected. Actual status code is {r.status_code}'


def test_delete_gist_by_id(gists_test_helper, gist):
    """
    1. Create gist.
    2. Delete it by id.
    3. Validate via GET API that gist doesn't exists.
    """
    r = gists_test_helper.delete_gist_by_id(gist)
    assert r.status_code == 204, f'Status code for delete gist is not as expected. Actual status code is {r.status_code}'
    r = gists_test_helper.get_gist_by_id(gist)
    assert r.status_code == 404, f'Status code for get deleted gist is not as expected. Actual status code is {r.status_code}'


def test_unauthorized_delete_gist_by_id_negative(gists_test_helper_non_authorized, gist):
    """
    1. Create gist.
    2. Try to delete it by id with no authorization.
    3. Validate an error.
    """
    r = gists_test_helper_non_authorized.delete_gist_by_id(gist)
    assert r.status_code == 404, f'Status code for delete gist is not as expected. Actual status code is {r.status_code}'


def test_delete_gist_by_invalid_id(gists_test_helper):
    """
    1. Try to delete gist by invalid id.
    2. Validate an error.
    """
    r = gists_test_helper.delete_gist_by_id('invalid_id')
    assert r.status_code == 404, f'Status code for delete non-existing gist is not as expected. Actual status code is {r.status_code}'


def test_get_gists_for_user(gists_test_helper_non_authorized):
    """
    1. Create gist.
    2. Get gists list by `user` param.
    3. Validate response.
    """
    r = gists_test_helper_non_authorized.get_gists_by_user(user=gists_test_helper_non_authorized.git_hub_user)
    assert r.status_code == 200, f'Status code for get gists by user is not as expected. Actual status code is {r.status_code}'
    results = r.json()
    assert all(gist['owner']['login'] == gists_test_helper_non_authorized.git_hub_user for gist in results), 'gist for another user were returned in get by user response'


def test_get_gists_for_invalid_user(gists_test_helper_non_authorized):
    """
    1. Try to get gists by non-existing user.
    2. Validate an error.
    """
    r = gists_test_helper_non_authorized.get_gists_by_user(user='notExistingGitHubUser')
    assert r.status_code == 404
    assert r.json() == {'documentation_url': 'https://docs.github.com/rest/reference/gists#list-gists-for-a-user',
        'message': 'Not Found'}


def test_get_gists_by_user_per_page_parameter(gists_test_helper_non_authorized):
    """
    1. Get gists by user using `per_page` query params.
    2. Validate response according to query params.
    """
    r = gists_test_helper_non_authorized.get_gists_by_user(user=gists_test_helper_non_authorized.git_hub_user, query_params='since=2000-01-01T00:00:00Z&per_page=40&page=1')
    assert r.status_code == 200, f'Status code for get gists by user is not as expected. Actual status code is {r.status_code}'
    result = r.json()
    assert len(result) == 40, "Number of gists doesn't equals to `per_page` parameter."


def test_get_gists_by_user_page_parameter(gists_test_helper_non_authorized):
    """
    1. Get 2 gists on one page.
    2. Get 1 gist on second page.
    3. Validate gist from second page equals to second gist from previous result.
    """
    r = gists_test_helper_non_authorized.get_gists_by_user(user=gists_test_helper_non_authorized.git_hub_user, query_params='since=2000-01-01T00:00:00Z&per_page=2&page=1')
    assert r.status_code == 200, f'Status code for get gists by user is not as expected. Actual status code is {r.status_code}'
    one_page_gists = r.json()
    r = gists_test_helper_non_authorized.get_gists_by_user(user=gists_test_helper_non_authorized.git_hub_user, query_params='since=2000-01-01T00:00:00Z&per_page=1&page=2')
    assert r.status_code == 200, f'Status code for get gists by user is not as expected. Actual status code is {r.status_code}'
    second_gist = r.json()
    assert second_gist[0] == one_page_gists[1], 'get gists by user with `page` param returns invalid result'


def test_get_gists_by_user_with_invalid_date_negative(gists_test_helper_non_authorized):
    """
    1. Try to get gists by user using invalid `since` query params.
    2. Validate empty response.
    """
    r = gists_test_helper_non_authorized.get_gists_by_user(user=gists_test_helper_non_authorized.git_hub_user, query_params='since=2100-01-01T00:00:00Z&per_page=40&page=1')
    assert r.status_code == 200, f'Status code for get gists by user is not as expected. Actual status code is {r.status_code}'
    assert not r.json()
