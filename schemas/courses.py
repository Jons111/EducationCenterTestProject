from pydantic import BaseModel


class CoursesBase(BaseModel):
    name: str
    period: int
    price: int


class CoursesCreate(CoursesBase):
    pass


class CoursesUpdate(CoursesBase):
    id: int
    status: bool
