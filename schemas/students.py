from pydantic import BaseModel


class StudentsBase(BaseModel):
    name: str
    number: str


class StudentsCreate(StudentsBase):
    pass


class StudentsUpdate(StudentsBase):
    id: int
    status: bool
