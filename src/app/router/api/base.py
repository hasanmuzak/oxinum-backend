from fastapi import APIRouter
from router.api.user_routes import user__base
from router.api.currency_routes import currency__base

base_router = APIRouter()
base_prefix = '/api'


base_router.include_router(user__base.base_router, prefix=base_prefix)
base_router.include_router(currency__base.base_router, prefix=base_prefix)


@base_router.get('/')
def index():
    return {
        'detail' : f"Welcome to Oxinum's REST API. For URL patterns, visit /docs..."
    }
 