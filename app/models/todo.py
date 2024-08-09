from sqlalchemy import Column, Integer, String, DateTime, create_engine
from app.db_setting.db_base import Base

class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    deadline = Column(DateTime)
    status = Column(String)
