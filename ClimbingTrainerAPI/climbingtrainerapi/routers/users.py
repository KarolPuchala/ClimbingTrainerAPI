from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from climbingtrainerapi.database import get_db
from climbingtrainerapi.repositories.users import create, delete_one, fetch_one, update_by_id

from climbingtrainerapi.schemas.users import UserSchema

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', status_code=201)
async def add(user: UserSchema, db: Session = Depends(get_db)):
    create(
        db=db,
        name=user.name,
        email=user.email,
        password=user.password,
    )


@router.get("/{user_id}")
async def get(user_id: int, db: Session = Depends(get_db)) -> UserSchema:
    return fetch_one(db=db, user_id=user_id)


@router.delete("/{user_id}")
async def delete(user_id: int, db: Session = Depends(get_db)) -> UserSchema:
    return delete_one(db=db, user_id=user_id)


@router.put("/{user_id}")
async def update(user_id: int, user: UserSchema, db: Session = Depends(get_db)) -> UserSchema:
    return update_by_id(db=db, user_id=user_id, **user.model_dump())
