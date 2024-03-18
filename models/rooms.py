from sqlalchemy import Column, Integer, String, Boolean,  ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from db import Base


class Rooms(Base):
    __tablename__ = "Rooms"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    number = Column(String(30), nullable=True)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
