from sqlalchemy import Column, Integer, String, Boolean, Float, Text, DateTime, func,ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Groups(Base):
    __tablename__ = "Groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('Rooms.id'), nullable=False)
    time_id = Column(Integer, ForeignKey('Times.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    days = Column(String(30), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer,ForeignKey('Users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
