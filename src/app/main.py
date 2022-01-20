from typing import Optional
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

# Router
from router.api import base as BaseApiRouter

# Helper Library
from lib import binance
from db.config import Session
from db.config import Base, engine
import cronjob


Base.metadata.create_all(bind=engine)


app = FastAPI()
# Scheduling Tasks

@app.on_event("startup")
@repeat_every(seconds=5)
def fetch_price_and_save():
    cronjob.price.get_price_and_save(Session())

app.include_router(BaseApiRouter.base_router)



