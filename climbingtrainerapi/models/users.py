from sqlalchemy import Column, Integer, String
from climbingtrainerapi.database import Base, engine

Base.metadata.create_all(engine)


class User(Base):
    __tablename__  = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
