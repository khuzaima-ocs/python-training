from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from database import engine
import models
from controllers import auth, todos
from middlewares import exception as ExceptionMiddleware 

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/raise-handled-exception')
def raise_handled_exception():
    try:
        result = ExceptionMiddleware.raise_exception()
        return PlainTextResponse(f"The result is {str(result)}.")
    except Exception as e:
        return HTTPException(
            status_code=500,
            detail = f"Something went wrong in the api call.\nERROR: {str(e)}" 
        ) 
    
@app.get('/raise-unhandled-exception')
def raise_unhandled_exception():
    result = ExceptionMiddleware.raise_exception()
    return PlainTextResponse(f"The result is {str(result)}.")
    
app.include_router(auth.router)
app.include_router(todos.router)

@app.exception_handler(Exception)
async def handle_exceptions(request: Request, exc: Exception):
     return JSONResponse(
        status_code=500,
        content={"detail": f"Something went wrong. Try again later.\nERROR: {str(exc)}"}
    )