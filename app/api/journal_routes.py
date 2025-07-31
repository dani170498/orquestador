from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.core.deps import get_db
from app.db.models.journal_contable import JournalContable
from app.db.models.transacciones_contables import TransaccionContable

router = APIRouter()

# 📄 Listar todos los journals con todos los campos
@router.get("/journals")
def list_journals(db: Session = Depends(get_db)):
    journals = db.execute(select(JournalContable)).scalars().all()

    return [
        {
            "id": j.id,
            "periodo": j.periodo,
            "id_contable": j.id_contable,
            "codificador": j.codificador,
            "no_journal": j.no_journal,
            "boa": j.boa,
            "razon_journal": j.razon_journal,
            "documento_elaborador": j.documento_elaborador,
            "documento_autorizacion": j.documento_autorizacion,
            "fecha_creacion": j.fecha_creacion,
            "estado": j.estado,
            "log_proceso": j.log_proceso,
            "json_original": j.json_original,
            "json_transformado": j.json_transformado,
        }
        for j in journals
    ]


# 📄 Obtener TODAS las transacciones de un journal
@router.get("/journals/{journal_id}")
def get_journal_transactions(journal_id: int, db: Session = Depends(get_db)):
    transactions = db.execute(
        select(TransaccionContable).where(TransaccionContable.journal_id == journal_id)
    ).scalars().all()

    return [
        {
            #"id": t.id,
            "journal_id": t.journal_id,
            #"line": t.line,
            "layout_id": t.layout_id,
            "transaction_ref": t.transaction_ref,
            "currency": t.currency,
            "date": t.date,
            "description": t.description,
            "account_code": t.account_code,
            "transaction_amount": t.transaction_amount,
            "memo_amount": t.memo_amount,
            "l1_cost_centre": t.l1_cost_centre,
            "l2_funder": t.l2_funder,
            "l3_project": t.l3_project,
            "l4_donor_reporting_line": t.l4_donor_reporting_line,
            "l5_tax": t.l5_tax,
            "l6_supplier": t.l6_supplier,
        }
        for t in transactions
    ]
