from typing import Optional

from pydantic import BaseModel
from pydantic.datetime_parse import date


class RoomsBase(BaseModel):
    name: date
    number: Optional[int]=0


class RoomsCreate(RoomsBase):
    pass


class RoomsUpdate(RoomsBase):
    id: int
    status: bool
