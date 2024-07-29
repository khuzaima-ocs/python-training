from fastapi import FastAPI
from sockets import sio_app

app = FastAPI()

app.mount('/', app=sio_app)
