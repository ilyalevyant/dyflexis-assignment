from dataclasses import dataclass

from test_helpers.booking_service_api import BookingServiceApi
from test_helpers.common_functions import create_query_by_params


@dataclass
class BookingService(BookingServiceApi):

    def __post_init__(self):
        self.base_endpoint = self.booking_conf.service_endpoint
        self.ping_endpoint = f"{self.base_endpoint}/ping"
        self.booking_endpoint = f"{self.base_endpoint}/booking"

        self.booking_ids = []


    def ping(self):
        r = self.booking_service_get(self.ping_endpoint)
        return r

    def get_bookings(self, params: list = None):
        if params:
            query = create_query_by_params(params)
            self.booking_endpoint += query
        r = self.booking_service_get(self.booking_endpoint)
        return r

    def get_booking(self, id: str):
        r = self.booking_service_get(f'{self.booking_endpoint}/{id}')
        return r

    def create_booking(self, payload):
        r = self.booking_service_post(self.booking_endpoint, payload)
        return r

    def update_booking(self, id, payload):
        r = self.booking_service_put(f'{self.booking_endpoint}/{id}', payload)
        return r

    def partial_update_booking(self, id, payload):
        r = self.booking_service_patch(f'{self.booking_endpoint}/{id}', payload)
        return r

    def delete_booking(self, id):
        r = self.booking_service_delete(f'{self.booking_endpoint}/{id}')
        return r
