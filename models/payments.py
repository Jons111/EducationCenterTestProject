from sqlalchemy import Column, Integer, String, Boolean, Float, Text, DateTime, func,ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Payments(Base):
    __tablename__ = "Payments"
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('Groups.id'), nullable=False)
    student_group_id = Column(Integer, ForeignKey('GroupStudents.id'), nullable=False)
    type = Column(String(30), nullable=True)
    money = Column(Float, nullable=False)
    payment_number = Column(String(30), nullable=True)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer,ForeignKey('Users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
