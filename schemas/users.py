from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    number: str
    roll: str
    username: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    id: int
    kpi: float
    salary: float
    status: bool
