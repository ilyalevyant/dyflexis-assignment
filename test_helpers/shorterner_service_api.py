from dataclasses import dataclass
from test_helpers.services_api import ServicesApi
from test_helpers.config import Config


@dataclass
class ShorternerServiceApi(ServicesApi):
    shorterner_conf: Config

    def shorterner_service_get(self, endpoint):
        r = self.get(endpoint)
        return r

    def shorterner_service_post(self, endpoint, payload=None):
        r = self.post(endpoint, payload)
        return r

    def shorterner_service_delete(self, endpoint):
        r = self.delete(endpoint)
        return r
