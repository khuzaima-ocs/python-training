from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import middlewares.auth as AuthMiddleware
import dtos, models
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post('/signup')
async def sign_up(user: dtos.User_dto, db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.email == user.email).first()

    if db_user:
        raise HTTPException(status_code=401, detail="User already exists.")
    
    new_user = models.Users()
    new_user.name = user.name
    new_user.email = user.email
    new_user.password = AuthMiddleware.hash_password(user.password)

    db.add(new_user)
    db.commit()

    return {
        "message": "User created successfully"
    }

@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = AuthMiddleware.authenticate_user(form.username, form.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials.")
    
    return AuthMiddleware.generate_token(user.email, user.id)