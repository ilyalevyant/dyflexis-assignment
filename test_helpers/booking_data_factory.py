from dataclasses import dataclass
from test_helpers.common_functions import load_json_schema
from copy import deepcopy


@dataclass
class BookingDataFactory:
    __create_booking_payload = load_json_schema('schemas/create_booking_payload.json')
    __update_booking_payload = load_json_schema('schemas/update_booking_payload.json')

    def create_booking_payload(self, rnd_value: str = '') -> dict:
        """create payload for new booking"""
        payload: dict = deepcopy(self.__create_booking_payload)
        for k in ['firstname', 'lastname']:
            payload[k] += rnd_value
        return payload

    def update_booking_payload(self) -> dict:
        return deepcopy(self.__update_booking_payload)
