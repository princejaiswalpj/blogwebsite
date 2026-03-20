from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models,schemas
from typing import List
from database import get_db 


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
