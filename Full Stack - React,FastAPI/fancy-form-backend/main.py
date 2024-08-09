import base64
import os
from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy import or_
from fastapi.middleware.cors import CORSMiddleware
import models, dtos, utils
from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

models.Base.metadata.create_all(bind=engine)

@app.post('/signup')
async def sign_up(user_data: dtos.User_request_dto = Depends(dtos.User_request_dto.as_form), file: UploadFile = File, db: Session = Depends(get_db)):
    try:
        uploaded_file_path = await utils.save_image(file)
        if uploaded_file_path is None:
            return JSONResponse(
                status_code=500,
                content="Error saving image file."
            )
        
        user = models.User()
        user.first_name = user_data.firstName
        user.last_name = user_data.lastName
        user.username = user_data.username
        user.email = user_data.email.lower()
        user.password = user_data.password
        if uploaded_file_path:
            user.display_pic = uploaded_file_path

        db.add(user)
        db.commit()

        return JSONResponse(
            status_code=201,
            content= "User saved successfully."
        )
    
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=str(e)
        )
    
@app.get('/users' , response_model=list[dtos.User_resposne_dto])
async def get_users(search_query: str = "", db: Session = Depends(get_db)):
    query = db.query(models.User)
    if search_query:
        query = query.filter(
            or_(
                models.User.email.ilike(f"%{search_query}%"),
                models.User.username.ilike(f"%{search_query}%")
            )
        )
    users = query.all()
    for user in users:
        user.display_pic = user.display_pic.split('uploads\\')[1]

    return users
    

@app.get("/image/{image_name}")
async def get_image(image_name: str):
    image_path = os.path.join("uploads", image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        return {"error": "Image not found"}