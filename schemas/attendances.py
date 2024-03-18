from pydantic import BaseModel
from pydantic.datetime_parse import date


class CoursesBase(BaseModel):
    student_id: int
    check: bool
    day: date


class CoursesCreate(CoursesBase):
    pass


class CoursesUpdate(CoursesBase):
    id: int
    status: bool
