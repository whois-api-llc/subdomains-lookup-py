import copy
from datetime import datetime

from .base import BaseModel
import sys

if sys.version_info < (3, 9):
    import typing


def _datetime_from_int(values: dict, key: str) -> datetime or None:
    if key in values and values[key]:
        return datetime.utcfromtimestamp(values[key])
    return None


def _string_value(values: dict, key: str) -> str:
    if key in values and values[key]:
        return str(values[key])
    return ''


def _float_value(values: dict, key: str) -> float:
    if key in values and values[key]:
        return float(values[key])
    return 0.0


def _int_value(values: dict, key: str) -> int:
    if key in values and values[key]:
        return int(values[key])
    return 0


def _list_value(values: dict, key: str) -> list:
    if key in values and type(values[key]) is list:
        return copy.deepcopy(values[key])
    return []


def _list_of_objects(values: dict, key: str, classname: str) -> list:
    r = []
    if key in values and type(values[key]) is list:
        r = [globals()[classname](x) for x in values[key]]
    return r


def _bool_value(values: dict, key: str) -> bool:
    if key in values and values[key]:
        return bool(values[key])
    return False


class Record(BaseModel):
    domain: str
    first_seen: datetime or None
    last_seen: datetime or None

    def __init__(self, values):
        super().__init__()
        self.domain = ''
        self.first_seen = None
        self.last_seen = None

        if values:
            self.domain = _string_value(values, 'domain')
            self.first_seen = _datetime_from_int(values, 'firstSeen')
            self.last_seen = _datetime_from_int(values, 'lastSeen')


class Result(BaseModel):
    count: int
    if sys.version_info < (3, 9):
        records: typing.List[Record]
    else:
        records: [Record]

    def __init__(self, values):
        super().__init__()
        self.count = 0
        self.records = []

        if values is not None:
            self.count = _int_value(values, "count")
            self.records = _list_of_objects(values, "records", "Record")


class Response(BaseModel):
    _PAGE_SIZE = 300
    search: str
    result: Result or None

    def __init__(self, values):
        super().__init__()
        self.search = ''
        self.result = None

        if values is not None:
            self.search = _string_value(values, 'search')
            if 'result' in values:
                self.result = Result(values['result'])


class ErrorMessage(BaseModel):
    code: int
    message: str

    def __init__(self, values):
        super().__init__()

        self.code = 0
        self.message = ''

        if values is not None:
            self.code = _int_value(values, 'code')
            self.message = _string_value(values, 'messages')
