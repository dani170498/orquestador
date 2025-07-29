from app.core.database import SessionLocal
from sqlalchemy.orm import Session

# Dependencia para inyectar la DB en FastAPI
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
