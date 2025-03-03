from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import user as user_crud
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.get("/", response_model=List[User])
def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """Retrieve users"""
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(*, db: Session = Depends(get_db), user_in: UserCreate) -> Any:
    """Create new user"""
    user = user_crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )
    user = user_crud.get_user_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system.",
        )
    user = user_crud.create_user(db, user_in=user_in)
    return user


@router.get("/{user_id}", response_model=User)
def read_user(*, db: Session = Depends(get_db), user_id: int) -> Any:
    """Get user by ID"""
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.put("/{user_id}", response_model=User)
def update_user(*, db: Session = Depends(get_db), user_id: int, user_in: UserUpdate) -> Any:
    """Update a user"""
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    user = user_crud.update_user(db, db_user=user, user_in=user_in)
    return user


@router.delete("/{user_id}", response_model=User)
def delete_user(*, db: Session = Depends(get_db), user_id: int) -> Any:
    """Delete a user"""
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    user = user_crud.delete_user(db, user_id=user_id)
    return user