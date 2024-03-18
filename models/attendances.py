from sqlalchemy import Column, Integer, String, Boolean, Float, Text, DateTime, func,ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Attendances(Base):
    __tablename__ = "Attendances"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer,ForeignKey('GroupStudents.id'), nullable=False)
    check = Column(Boolean, nullable=False, default=None)
    day = Column(DateTime(timezone=True),   nullable=True)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer,ForeignKey('Users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
