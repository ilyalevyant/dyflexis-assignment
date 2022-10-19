from dataclasses import dataclass
from test_helpers.shorterner_service_api import ShorternerServiceApi


@dataclass
class ShorternerService(ShorternerServiceApi):

    def __post_init__(self):
        self.base_endpoint = self.shorterner_conf.service_endpoint
        self.create_shortcode_endpoint = f"{self.base_endpoint}/shorten"

    def create_shortcode(self, payload):
        r = self.shorterner_service_post(self.create_shortcode_endpoint, payload)
        return r

    def delete_shortcode(self, code):
        r = self.shorterner_service_delete(f"{self.base_endpoint}/{code}")
        return r

    def get_shorterner_stats(self, code):
        r = self.shorterner_service_get(f"{self.base_endpoint}/{code}/stats")
        return r

    def redirect(self, code):
        r = self.shorterner_service_get(f"{self.base_endpoint}/{code}")
        return r

    def assert_shorterner_stats(self, stats):
        for k in ['created', 'lastRedirect', 'redirectCount']:
            assert k in stats, f'filed "{k}" is not found in shorterner stats response'
