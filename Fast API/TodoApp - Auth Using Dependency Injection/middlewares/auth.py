from fastapi import Depends, HTTPException
from passlib.context import CryptContext
import models
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta

bcrypt = CryptContext(schemes=['bcrypt'], deprecated='auto')
auth_bearer = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "todo_app_secret_key"
ALGORITHM = "HS256"

def hash_password(password):
    return bcrypt.hash(password)

def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str, db: Session):
    user = db.query(models.Users).filter(models.Users.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    return user

def generate_token(email: str, user_id: str):
    to_encode = {
        "email": email,
        "user_id": user_id,
        "exp":  datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str = Depends(auth_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email = payload.get('email')
        id = payload.get('user_id')

        if not email or not id:
            raise Exception()
        
        return {
            "email": email,
            "id": id
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="User not found.")