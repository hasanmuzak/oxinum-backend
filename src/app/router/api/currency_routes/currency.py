from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.get_db import get_db
from typing import List
import cruds
from db.schemas.currency import CurrencyResponseSchema, CurrencyCreateFormSchema


router = APIRouter()


@router.get('/all', summary="get all currencies", tags=['admin/currency'], response_model=List[CurrencyResponseSchema])
def get_all_currencies(db: Session = Depends(get_db)):
    currencies = cruds.currency.get_all_currencies(db=db)
    if not currencies:
        raise HTTPException(
            400, detail="Görüntülenecek herhangi bir para birimi yok.")
    return currencies

@router.post('/create-currency', summary="create a currency", tags=['admin/currency'], response_model=CurrencyResponseSchema)
def get_all_currencies(json: CurrencyCreateFormSchema, db: Session = Depends(get_db)):
    return cruds.currency.put(db, data={
        "symbol": json.symbol,
        "title": json.title,
        "logo": json.logo
    })
