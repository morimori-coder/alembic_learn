from sqlalchemy import Column, Integer, String, create_engine
from app.db_setting.db_base import Base

class User2(Base):
    __tablename__ = 'users2'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
