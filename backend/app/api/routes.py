from fastapi import APIRouter

from app.api.v1 import users

router = APIRouter()

# Include all API v1 routers
router.include_router(users.router, prefix="/v1/users", tags=["users"])