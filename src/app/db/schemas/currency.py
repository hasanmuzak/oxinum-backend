from pydantic import BaseModel
from db.models.currency import Currency

from typing import Optional

class CurrencyCreateFormSchema(BaseModel):
    title: str
    symbol: str
    logo: Optional[str]

    class Config:
        orm_mode = True

class CurrencyResponseSchema(BaseModel):
    id: int
    title: str
    symbol: str
    logo: str = None

    class Config:
        orm_mode = True
