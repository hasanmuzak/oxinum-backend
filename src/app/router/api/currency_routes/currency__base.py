from fastapi import APIRouter
from router.api.currency_routes import currency

base_router = APIRouter()
base_prefix = '/currency'


base_router.include_router(currency.router, prefix=base_prefix)
