from sqlalchemy.orm import Session
from sqlalchemy import update
from climbingtrainerapi.models.users import User


def create(db: Session, name: str, email: str, password: str) -> User:
    db_user = User(name=name, email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def fetch_one(db: Session, user_id: int) -> User:
    return db.get(User, user_id)
