from sqlalchemy import Column, Integer, Float

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.db.config import Base


class RelUserCurrency(Base):
    __tablename__ = "rel_user_currencies"
    id= Column(Integer, primary_key=True)
    currency_id = Column(Integer, ForeignKey("currencies.id"), primary_key=True)
    currency = relationship("Currency", foreign_keys='RelUserCurrency.currency_id')
    balance = Column(Float, default=0.0)
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship("Currency", foreign_keys='RelUserCurrency.user_id')
