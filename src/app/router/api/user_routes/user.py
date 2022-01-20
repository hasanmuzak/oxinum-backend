from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.get_db import get_db
from passlib.context import CryptContext

# Import Models
from db.models.user import User

# Import Cruds
import cruds

# Import Response Schemas
from db.schemas.user import UserCreateResponseSchema

# Import Form Schemas
from db.schemas.user import UserCreateFormSchema

# Import Utils
router = APIRouter()


@router.post('/create-user', summary="get unpaid order list", tags=['admin/user'], response_model=UserCreateResponseSchema)
def create_user(data: UserCreateFormSchema, db: Session = Depends(get_db)):
    user = cruds.user.get_by_email(db, data.email)
    if user:
        raise HTTPException(
            400, 'Bu e-posta adresine ait kullanıcı bulunmakta.')
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(data.password)

    new_user = cruds.user.put(db, data={
        "email": data.email,
        "name": data.name,
        "password": hashed_password,
        "surname": data.surname,
        "created_at": data.created_at
    })

    return new_user
