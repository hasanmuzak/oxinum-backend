from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

# Models
from src.db.models.currency import Currency as CurrencyModel

def get_all_currencies(db: Session) -> List[CurrencyModel]:
    return db.query(CurrencyModel).all()

def put(db: Session, *, record: CurrencyModel = None, data: dict) -> CurrencyModel:
    try:
        record = record if record is not None else CurrencyModel()
        for key, value in data.items():
            setattr(record, key, value)

        db.add(record)
        db.commit()
        db.refresh(record)

        return record

    except SQLAlchemyError as e:
        raise HTTPException(400, detail=f"{e}")