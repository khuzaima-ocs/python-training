from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class Todo_dto(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="Priority must be b/w 1-5")
    completed: bool

class User_dto(BaseModel):
    name: str
    email: EmailStr 
    password: str = Field(min_length=6)
    