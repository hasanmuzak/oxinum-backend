from fastapi import APIRouter
from router.api.user_routes import user

base_router = APIRouter()
base_prefix = '/user'


base_router.include_router(user.router, prefix=base_prefix)
 