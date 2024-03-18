from pydantic import BaseModel


class PaymentsBase(BaseModel):
    group_id: int
    student_group_id: int
    type: str
    money: float
    


class PaymentsCreate(PaymentsBase):
    pass


class PaymentsUpdate(PaymentsBase):
    id: int
    status: bool
