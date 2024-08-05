from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB = 'sqlite'
# DB = 'mysql'
# DB = 'postgres'

engine = None
if DB == 'sqlite':
    engine = create_engine(
        "sqlite:///./todos.db" ,connect_args={"check_same_thread": False}
    )
elif DB == 'mysql':
    engine = create_engine(
        "mysql+pymysql://root:mysql@localhost:3306/todoApp"
    )
elif DB == 'postgres':
    engine = create_engine(
        "postgresql://postgres:postgres@localhost:5432/TodoAppDatabase"
    )

sessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()