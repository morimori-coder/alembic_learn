from sqlalchemy import Column, Integer, String, NVARCHAR
from app.db_setting.db_base import Base

class Person(Base):
    __tablename__ = 'PERSON'
    id = Column(Integer, primary_key=True)
    NAME = Column(NVARCHAR(128))
    WEIGHT = Column(Integer)
    HIGH = Column(Integer)
    AGE = Column(Integer)
