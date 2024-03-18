from sqlalchemy import Column, Integer, String, Boolean,  ForeignKey, DateTime, func,Time
from sqlalchemy.orm import relationship

from db import Base


class Times(Base):
    __tablename__ = "Times"
    id = Column(Integer, primary_key=True)
    from_time = Column(Time(timezone=True), nullable=False)
    to_time = Column(Time(timezone=True), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
