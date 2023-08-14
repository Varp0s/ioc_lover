from fastapi import APIRouter
from .endpoints import ioc

api_router = APIRouter()

api_router.include_router(ioc.router)
api_router.include_router(ioc.router, prefix="/search")



