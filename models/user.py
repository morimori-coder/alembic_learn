from sqlalchemy import Column, Integer, String, create_engine
from db_setting.db_base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
