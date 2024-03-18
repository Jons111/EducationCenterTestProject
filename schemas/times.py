from pydantic import BaseModel
from pydantic.datetime_parse import date


class TimesBase(BaseModel):
    from_time: date
    to_time: date


class TimesCreate(TimesBase):
    pass


class TimesUpdate(TimesBase):
    id: int
    status: bool
