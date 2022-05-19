from dataclasses import dataclass

from gists_service_api import GistsServiceApi


@dataclass
class GistsServiceHelper(GistsServiceApi):

    def __post_init__(self):
        self.git_hub_user = self.gists_conf.git_hub_user

        self.base_endpoint = self.gists_conf.service_endpoint
        self.gists_endpoint = f'{self.base_endpoint}/gists'

    def get_gists_by_user(self, user, query_params='per_page=30'):
        r = self.gists_service_get(f'{self.base_endpoint}/users/{user}/gists?{query_params}')
        return r

    def get_gist_by_id(self, gist_id):
        r = self.gists_service_get(f'{self.gists_endpoint}/{gist_id}')
        return r

    def create_gist(self, payload):
        r = self.gists_service_post(self.gists_endpoint, payload)
        return r

    def update_gist_by_id(self, payload, gist_id):
        r = self.gists_service_patch(f'{self.gists_endpoint}/{gist_id}', payload=payload)
        return r

    def delete_gist_by_id(self, gist_id):
        r = self.gists_service_delete(f'{self.gists_endpoint}/{gist_id}')
        return r
