from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base

class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('Users', back_populates='todos')


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50))

    todos = relationship('Todos', back_populates='owner')