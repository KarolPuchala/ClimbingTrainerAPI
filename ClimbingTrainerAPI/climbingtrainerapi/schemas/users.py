from typing import Optional
from pydantic import BaseModel, PositiveInt, Field, EmailStr


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str
    email: EmailStr
    disabled: Optional[bool] = False

    class Config:
        from_attributes = True


class UserInDB(UserSchema):
    hashed_password: str