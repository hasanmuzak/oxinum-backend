from sqlalchemy.orm import Session

# Import Models
from src.db.models.currency import Currency as CurrencyModel
from src.db.models.price_history import PriceHistory as PriceHistoryModel

from binance.client import Client
from sqlalchemy.exc import SQLAlchemyError

import dotenv
import os
import time
dotenv.load_dotenv()


def get_price_and_save(db: Session):
    currencies = db.query(CurrencyModel).all()
    client = Client(os.environ.get("API_KEY"), os.environ.get("API_SECRET"))
    if currencies:
        for i in currencies:
            data = client.get_ticker(symbol=i.symbol)
            price_history_model = PriceHistoryModel(created_at=str(int(time.time())), price=float(
                data["askPrice"]), volume=float(data["quoteVolume"]), currency_id=i.id)
            db.add(price_history_model)
            db.commit()
            time.sleep(0.2)
