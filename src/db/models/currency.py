from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.config import Base


class Currency(Base):
    __tablename__   = "currencies"
    id              = Column(Integer, primary_key=True)
    title           = Column(String, nullable=False, unique=True)
    symbol          = Column(String, nullable=False, unique=True)
    logo            = Column(String, nullable=True)

    