from fastapi import Request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine



def get_db(request: Request):
    return request.state.db


SQLALCHEMY_DATABASE_URL = "postgresql://project:project@localhost:6543/project"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()
