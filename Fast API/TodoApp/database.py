from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///./todos.db"

engine = create_engine(
    DB_URL ,connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()