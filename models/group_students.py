from sqlalchemy import Column, Integer, String, Boolean, Float, Text, DateTime, func,ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class GroupStudents(Base):
    __tablename__ = "GroupStudents"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer,ForeignKey('Students.id'), nullable=False)
    group_id = Column(Integer,ForeignKey('Groups.id'), nullable=False)
    balance = Column(Float, nullable=True, default=0)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer,ForeignKey('Users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
