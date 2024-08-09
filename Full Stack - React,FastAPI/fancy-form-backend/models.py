from sqlalchemy import Column, Integer, Boolean, String
from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(50))
    display_pic = Column(String)