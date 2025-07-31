import datetime
import json
from sqlalchemy.orm import Session
from app.db.models.journal_contable import JournalContable
from app.db.models.transacciones_contables import TransaccionContable

def save_crs_data_to_db(db: Session, data: dict):
    # 🔹 Acceder al objeto DATA del JSON
    journal_data = data.get("DATA", {})
    transactions = journal_data.get("transactions", [])

    # 1️⃣ Crear registro de journal
    new_journal = JournalContable(
        periodo=journal_data.get("periodo"),
        id_contable=journal_data.get("id_contable"),
        codificador=journal_data.get("codificador"),
        no_journal=journal_data.get("no_journal"),
        boa=journal_data.get("boa"),
        razon_journal=journal_data.get("razon_journal"),
        documento_elaborador=journal_data.get("documento_elaborador"),
        documento_autorizacion=journal_data.get("documento_autorizacion"),
        fecha_creacion=datetime.datetime.now(),
        estado="PENDIENTE",
        json_original=json.dumps(data, ensure_ascii=False)  # Guardar JSON completo para trazabilidad
    )

    db.add(new_journal)
    db.commit()
    db.refresh(new_journal)

    # 2️⃣ Insertar todas las transacciones
    for t in transactions:
        # Convertir valores opcionales
        fecha_tx = None
        if t.get("date"):
            try:
                fecha_tx = datetime.datetime.strptime(t.get("date"), "%d/%m/%Y").date()
            except ValueError:
                fecha_tx = None

        trans = TransaccionContable(
            journal_id=new_journal.id,
            line=t.get("line"),
            layout_id=t.get("layout_id"),
            transaction_ref=t.get("transaction_ref"),
            currency=t.get("currency"),
            date=fecha_tx,
            description=t.get("description"),
            account_code=t.get("account_code"),
            transaction_amount=float(t.get("transaction_amount") or 0),
            memo_amount=float(t.get("memo_amount") or 0),
            l1_cost_centre=t.get("l1_cost_centre"),
            l2_funder=t.get("l2_funder"),
            l3_project=t.get("l3_project"),
            l4_donor_reporting_line=t.get("l4_donor_reporting_line"),
            l5_tax=t.get("l5_tax"),
            l6_supplier=t.get("l6_supplier"),
        )

        db.add(trans)

    db.commit()

    return {
        "journal_id": new_journal.id,
        "transactions_inserted": len(transactions)
    }