from abc import ABC

import requests


class BaseMethod(ABC):

    def __init__(self, url):
        self.url = url

    def get(self, *, headers=None):
        response = requests.get(
            url=self.url,
            headers=headers
        )
        return response

    def post(self, *, payload, params=None, headers=None):
        response = requests.post(
            url=self.url,
            data=payload,
            params=params,
            headers=headers
        )
        return response

    def patch(self, *, payload, params=None, headers=None):
        response = requests.patch(
            url=self.url,
            data=payload,
            params=params,
            headers=headers
        )
        return response
