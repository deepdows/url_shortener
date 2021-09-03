from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "postgresql://user:secret@todo-db:5432/db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://SA6eP4SydD:lTqeHUpUYd@remotemysql.com:3306/SA6eP4SydD"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
