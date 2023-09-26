from pydantic import BaseModel, PositiveInt, Field, EmailStr


class UserSchema(BaseModel):
    id: PositiveInt
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    disabled: bool | None = None

    class Config:
        from_attributes = True
