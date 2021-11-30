from typing import Optional
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

# Router
from src.router.api import base as BaseApiRouter

# Helper Library
from src.lib import binance
from src.db.config import Session
from src import cronjob


# config.Base.metadata.create_all(bind=config.engine)


app = FastAPI()
# Scheduling Tasks

@app.on_event("startup")
@repeat_every(seconds=5)
def fetch_price_and_save():
    cronjob.price.get_price_and_save(Session())

app.include_router(BaseApiRouter.base_router)



