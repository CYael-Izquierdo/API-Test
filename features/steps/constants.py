from enum import Enum


class Constants:
    BASE_URL = 'http://192.168.64.2/'
    API_KEY = 'c278b5e3cca993d48a760aae98c8c81e108bb64f'
    CONTENT_TYPE = 'application/json'

    class StatusCode(Enum):
        CREATED = 201
        UNPROCESSABLE_ENTITY = 422
        OK = 200
        NOT_FOUND = 404
