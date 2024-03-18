from pydantic import BaseModel


class GroupStudentsBase(BaseModel):
    student_id: int
    group_id: int


class GroupStudentsCreate(GroupStudentsBase):
    pass


class GroupStudentsUpdate(GroupStudentsBase):
    id: int
    status: bool
