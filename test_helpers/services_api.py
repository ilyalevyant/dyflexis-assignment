from dataclasses import dataclass

import requests


@dataclass
class ServicesApi:
    __headers: dict

    def get(self, endpoint):
        r = requests.get(endpoint, headers=self.__headers)
        return r

    def post(self, endpoint, payload=None):
        r = requests.post(endpoint, headers=self.__headers, json=payload)
        return r

    def delete(self, endpoint):
        r = requests.delete(endpoint, headers=self.__headers)
        return r
