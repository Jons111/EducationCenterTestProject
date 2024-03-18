from pydantic import BaseModel


class GroupsBase(BaseModel):
    name: str
    course_id: int
    room_id: int
    time_id: int
    teacher_id: int
    days: str


class GroupsCreate(GroupsBase):
    pass


class GroupsUpdate(GroupsBase):
    id: int
    status: bool
