from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db.config import Base


class PriceHistory(Base):
    __tablename__ = "price_history"
    id = Column(Integer, primary_key=True)
    created_at = Column(String(13), nullable=False)
    price = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)

    currency_id = Column(Integer, ForeignKey("currencies.id"))
    currency = relationship("Currency", foreign_keys='PriceHistory.currency_id')
