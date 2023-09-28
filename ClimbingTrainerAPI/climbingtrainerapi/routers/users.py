from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from climbingtrainerapi.database import get_db
from climbingtrainerapi.repositories.users import create, delete_one, fetch_one, get_user_by_username, update_by_id

from climbingtrainerapi.schemas.users import UserSchema, UserInDB

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = 'abc'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(db, username: str, password: str) -> UserInDB | bool:
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password(password: str) -> str:
    return pwd_context.hash(password)


@router.post("/token")
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="INcorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta= access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/', status_code=201)
async def add(user: UserSchema, db: Session = Depends(get_db)):
    hashed_password = get_password(user.password)
    new_user = create(
        db,
        user.username,
        hashed_password,
        user.email,
        user.disabled,
    )

    return {
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'disabled': new_user.disabled
    }


@router.get("/{user_id}")
async def get(user_id: int, db: Session = Depends(get_db)) -> UserSchema:
    return fetch_one(db=db, user_id=user_id)


@router.delete("/{user_id}")
async def delete(user_id: int, db: Session = Depends(get_db)) -> UserSchema:
    return delete_one(db=db, user_id=user_id)


@router.put("/{user_id}")
async def update(user_id: int, user: UserSchema, db: Session = Depends(get_db)) -> UserSchema:
    return update_by_id(db=db, user_id=user_id, **user.model_dump())
