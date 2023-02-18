from dataclasses import dataclass
from test_helpers.services_api import ServicesApi
from test_helpers.config import Config


@dataclass
class BookingServiceApi(ServicesApi):
    booking_conf: Config

    def booking_service_get(self, endpoint):
        r = self.get(endpoint)
        return r

    def booking_service_post(self, endpoint, payload=None):
        r = self.post(endpoint, payload)
        return r

    def booking_service_put(self, endpoint, payload=None):
        r = self.put(endpoint, payload)
        return r

    def booking_service_patch(self, endpoint, payload=None):
        r = self.put(endpoint, payload)
        return r

    def booking_service_delete(self, endpoint):
        r = self.delete(endpoint)
        return r
