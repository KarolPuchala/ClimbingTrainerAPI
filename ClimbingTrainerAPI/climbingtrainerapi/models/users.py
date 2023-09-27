from sqlalchemy import Column, Integer, String, Boolean
from climbingtrainerapi.database import Base


class User(Base):
    __tablename__  = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    email = Column(String)
    disabled = Column(Boolean)
