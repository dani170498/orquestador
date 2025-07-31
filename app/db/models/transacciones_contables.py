from sqlalchemy import Column, Integer, String, Text, Date, DECIMAL, ForeignKey
from app.core.database import Base

class TransaccionContable(Base):
    __tablename__ = "transacciones_contables"
    __table_args__ = {"schema": "data"}

    id = Column(Integer, primary_key=True, index=True)
    journal_id = Column(Integer, ForeignKey("data.journal_contable.id", ondelete="CASCADE"))
    line = Column(Integer)
    layout_id = Column(String(100))
    transaction_ref = Column(String(100))
    currency = Column(String(10))
    date = Column(Date)
    description = Column(Text)
    account_code = Column(String(50))
    transaction_amount = Column(DECIMAL(18, 2))
    memo_amount = Column(DECIMAL(18, 2))
    l1_cost_centre = Column(String(100))
    l2_funder = Column(String(100))
    l3_project = Column(String(100))
    l4_donor_reporting_line = Column(String(100))
    l5_tax = Column(String(100))
    l6_supplier = Column(String(100))