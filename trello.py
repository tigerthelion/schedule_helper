
from requests import Session
import os
from dotenv import load_dotenv
load_dotenv()

registry = {}


class ResourceMeta(type):

    def __new__(metacls, name, bases, attrs):
        registry[name] = super().__new__(
            metacls, name, bases, attrs)
        return registry[name]


class Board(metaclass=ResourceMeta):
    def __init__(self):
        super().__init__()
        self.sub_url = "boards"

    def params(self):
        p = dict(param1='test1', param2='test2')

        p.update(self.base.auth_params())
        return "&".join([f"{k}={v}" for k, v in p.items()])

    def get(self, id):
        pass

    @property
    def resource_url(self):
        return f"https://{self.base._base_url}/{self.base._api_version}/{self.sub_url}"


class Trello:
    def __init__(self):
        for r, v in registry.items():
            setattr(self, r, v())
            v.base = self

        self._base_url = "api.trello.com"
        self._token = None
        self._api_key = None

        self._api_version = 1

    def set_auth(self, api_key, token):
        self._api_key = api_key
        self._token = token

    def auth_params(self):
        return dict(key=self._api_key, token=self._token)

    def send(self):
        pass
