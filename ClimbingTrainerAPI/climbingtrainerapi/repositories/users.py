from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import update
from climbingtrainerapi.models.users import User


def create(db: Session, username: str, hashed_password: str, email: str, disabled: bool = False) -> User:
    db_user = User(username=username, hashed_password=hashed_password, email=email, disabled=disabled)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def fetch_one(db: Session, user_id: int) -> User:
    return db.get(User, user_id)


def delete_one(db: Session, user_id: int):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return db.query(User).all()


def update_by_id(db: Session, user_id: int, **kwargs):
    del kwargs['id']
    db_user = db.execute(update(User).where(User.id == user_id).values(**kwargs))
    db.commit()
    return db_user
