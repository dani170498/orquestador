from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from app.core.database import Base

class JournalContable(Base):
    __tablename__ = "journal_contable"
    __table_args__ = {"schema": "data"}

    id = Column(Integer, primary_key=True, index=True)
    periodo = Column(String(50))
    id_contable = Column(String(100))
    codificador = Column(String(100))
    no_journal = Column(String(100))
    boa = Column(String(100))
    razon_journal = Column(Text)
    documento_elaborador = Column(String(100))
    documento_autorizacion = Column(String(100))
    fecha_creacion = Column(DateTime)
    estado = Column(String(50))
    log_proceso = Column(Text)
    json_original = Column(JSON)
    json_transformado = Column(JSON)