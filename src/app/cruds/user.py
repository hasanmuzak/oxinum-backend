from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

# Models
from db.models.user import User as UserModel


def put(db: Session, *, record: UserModel = None, data: dict) -> UserModel:
    try:
        record = record if record is not None else UserModel()
        for key, value in data.items():
            setattr(record, key, value)

        db.add(record)
        db.commit()
        db.refresh(record)

        return record

    except SQLAlchemyError as e:
        raise HTTPException(400, detail=f"{e}")


def get_by_email(db: Session, email: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.email == email).first()
