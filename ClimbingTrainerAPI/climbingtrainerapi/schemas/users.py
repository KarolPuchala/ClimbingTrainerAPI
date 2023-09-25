from pydantic import BaseModel, PositiveInt, Field, EmailStr


class UserSchema(BaseModel):
    id: PositiveInt
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
