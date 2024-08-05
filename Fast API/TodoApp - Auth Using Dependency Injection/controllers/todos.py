from fastapi import APIRouter, Depends, HTTPException
import models, dtos
from sqlalchemy.orm import Session
from database import get_db
from middlewares import auth as AuthMiddleware

router = APIRouter()

@router.get('/')
async def get_all_todos(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()

@router.get('/todos')
async def get_todos_by_user(user: dict = Depends(AuthMiddleware.decode_token), db: Session = Depends(get_db)):
    todos = db.query(models.Todos).filter(models.Todos.owner_id == user.get('id')).all()
    return todos

@router.post('/')
async def add_todo(todo: dtos.Todo_dto, user: dict = Depends(AuthMiddleware.decode_token), db: Session = Depends(get_db)):
    todo_obj = models.Todos()
    todo_obj.title = todo.title
    todo_obj.description = todo.description
    todo_obj.priority = todo.priority
    todo_obj.completed = todo.completed
    todo_obj.owner_id = user.get('id')

    db.add(todo_obj)
    db.commit()

    return {
        "message": "Saved Successfully!"
    }

@router.get('/{id}')
async def get_todo(id: int, user: dict = Depends(AuthMiddleware.decode_token),  db: Session = Depends(get_db)):
    todo = db.query(models.Todos).filter(models.Todos.id == id and models.Todos.owner_id == user.get('id')).first()
    return todo if todo else HTTPException(status_code=404, detail=f"Todo with id {id} not found")

@router.put('/{id}')
async def edit_todo(id: int, todo: dtos.Todo_dto, user: dict = Depends(AuthMiddleware.decode_token), db: Session = Depends(get_db)):
    todo_obj = db.query(models.Todos).filter(models.Todos.id == id and models.Todos.owner_id == user.get('id')).first()

    if not todo_obj:
        raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")

    todo_obj.title = todo.title
    todo_obj.description = todo.description
    todo_obj.priority = todo.priority
    todo_obj.completed = todo.completed

    db.add(todo_obj)
    db.commit()

    return {
        "message": "Edited Successfully!"
    }

@router.delete('/{id}')
async def delete_todo(id: int, user: dict = Depends(AuthMiddleware.decode_token), db: Session = Depends(get_db)):
    todo_obj = db.query(models.Todos).filter(models.Todos.id == id and models.Todos.owner_id == user.get('id')).first()
    if not todo_obj:
        raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")

    db.query(models.Todos).filter(models.Todos.id == id).delete()
    db.commit()

    return {
        "message": "Deleted Successfully!"
    }
    