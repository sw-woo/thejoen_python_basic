from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base

class Post(Base):
    __tablename__="posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())