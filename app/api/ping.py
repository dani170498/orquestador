from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.core.deps import get_db

router = APIRouter()

@router.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).scalar()
    return {"db": "ok" if result == 1 else "fail"}