from dataclasses import dataclass
from test_helpers.common_functions import load_json_schema
from copy import deepcopy


@dataclass
class ShorternerDataFactory:
    __create_shorterner_payload = load_json_schema('schemas/create_shorterner_payload.json')

    def create_shorterner_payload(self, url, shortcode=None):
        """create payload for new shorterner"""
        payload = deepcopy(self.__create_shorterner_payload)
        payload['url'] = url
        if shortcode:
            payload['shortcode'] = shortcode
        return payload
