from dataclasses import dataclass

from config import Config
from services_api import ServicesApi


@dataclass
class GistsServiceApi(ServicesApi):
    gists_conf: Config

    def gists_service_get(self, endpoint):
        r = self.get(endpoint)
        return r

    def gists_service_post(self, endpoint, payload=None):
        r = self.post(endpoint, payload)
        return r

    def gists_service_put(self, endpoint, payload=None):
        r = self.put(endpoint, payload)
        return r

    def gists_service_patch(self, endpoint, payload=None):
        r = self.patch(endpoint, payload)
        return r

    def gists_service_delete(self, endpoint):
        r = self.delete(endpoint)
        return r
