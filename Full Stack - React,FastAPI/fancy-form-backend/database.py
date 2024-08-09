from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "sqlite:///./fancyform.db" ,connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()