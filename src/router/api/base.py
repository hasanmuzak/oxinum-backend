from fastapi import APIRouter
from src.router.api.user_routes import user__base
from src.router.api.currency_routes import currency__base

base_router = APIRouter()
base_prefix = '/api'


base_router.include_router(user__base.base_router, prefix=base_prefix)
base_router.include_router(currency__base.base_router, prefix=base_prefix)
 