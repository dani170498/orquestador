from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.core.database import Base

class TokenAPI(Base):
    __tablename__ = "tokens_api"
    __table_args__ = {"schema": "data"}

    id = Column(Integer, primary_key=True, index=True)
    sistema = Column(String(50), nullable=False)
    token = Column(Text, nullable=False)
    expiracion = Column(DateTime, nullable=False)
    creado_en = Column(DateTime, server_default=func.now())
