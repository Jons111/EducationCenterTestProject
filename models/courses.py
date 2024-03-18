from sqlalchemy import Column, Integer, String, Boolean, Float, Text, DateTime, func,ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Courses(Base):
    __tablename__ = "Courses"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    period = Column(Float, nullable=True)
    price = Column(Float, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer,ForeignKey('Users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
