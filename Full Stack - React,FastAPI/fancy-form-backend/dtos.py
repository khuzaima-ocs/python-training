from fastapi import Form
from pydantic import BaseModel

class User_request_dto(BaseModel):
    firstName: str
    lastName: str
    email: str
    username: str
    password: str

    @classmethod
    def as_form(
        cls,
        firstName:str = Form(...),
        lastName: str = Form(...),
        email: str = Form(...),
        username: str = Form(...),
        password: str = Form(...)
    ):
        return cls(firstName=firstName, lastName=lastName, email=email, username=username, password=password)

class User_resposne_dto(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    display_pic: str