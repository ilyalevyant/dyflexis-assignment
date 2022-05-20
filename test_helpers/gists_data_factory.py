from dataclasses import dataclass
from test_helpers.common_functions import load_json_schema
from copy import deepcopy


@dataclass
class GistsDataFactory:
    __create_gist_payload = load_json_schema('schemas/create_gist_payload.json')
    __create_gist_expected_result = load_json_schema('schemas/create_gist_expected_result.json')
    __update_gist_payload = load_json_schema('schemas/update_gist_payload.json')

    def create_gist_payload(self, field_to_remove=None):
        """create paylod for new gist"""
        payload = deepcopy(self.__create_gist_payload)
        if field_to_remove:
            del(payload[field_to_remove])
        return payload

    def update_gist_payload(self):
        """create paylod for new gist"""
        payload = deepcopy(self.__update_gist_payload)
        return payload

    def create_gist_expected_result(self, non_mandatory_filed=None):
        """create paylod for new gist"""
        payload = deepcopy(self.__create_gist_expected_result)
        if non_mandatory_filed:
            key, value = non_mandatory_filed
            payload[key] = value
        return payload

    def create_gist_response(self, payload):
        """modifying actual result, delete dynamic data in response for create gists"""
        assert payload['updated_at']
        del(payload['updated_at'])
        return payload

    def actual_result_create_gist(self, payload):
        """modifying actual result, delete all dynamic data, that can't be tested automatically"""
        for key in ['url', 'forks_url', 'commits_url', 'id', 'git_pull_url', 'git_push_url', 'html_url', 'created_at', 'updated_at', 'comments_url', 'node_id']:
            assert payload[key], f"{key} doesn't exists in response for create gist"
            del(payload[key])
        for key in ['committed_at', 'url', 'version']:
            assert (payload['history'][0][key]), f"{key} doesn't exists in response['history'] for create gist"
            del(payload['history'][0][key])
        assert(payload['files']['some_test_file']['raw_url'])
        del(payload['files']['some_test_file']['raw_url'])
        return payload
