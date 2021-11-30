from pydantic import BaseModel
from src.db.models.user import User

class UserCreateResponseSchema(BaseModel):
    id          : int
    name        : str
    surname     : str
    email       : str
    class Config:
        orm_mode = True

class UserCreateFormSchema(BaseModel):
    name        : str
    surname     : str
    password    : str
    email       : str
    created_at  : str

    class Config:
        orm_mode = True