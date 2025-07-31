from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.deps import get_db
from crs.auth import get_token
from crs.fetch_data import get_crs_data
from app.services.crs_service import save_crs_data_to_db

router = APIRouter()

# ✅ Endpoint para obtener el token y su expiración
@router.get("/crs/token")
async def get_crs_token():
    token, expiracion = await get_token()
    return {
        "token": token,
        "expiracion": expiracion,
        "message": "Token obtenido exitosamente"
    }

# ✅ Endpoint para hacer fetch dinámico y guardar en BD
@router.post("/crs/fetch")
async def fetch_and_store_crs_data(
    location_id: int = Query(..., description="ID de la ubicación CRS"),
    start_date: str = Query(..., description="Fecha inicio DD/MM/YYYY"),
    end_date: str = Query(..., description="Fecha fin DD/MM/YYYY"),
    db: Session = Depends(get_db)
):
    # 1️⃣ Obtener data del CRS usando token persistente
    data = await get_crs_data(location_id, start_date, end_date)

    if not data:
        return {"status": "error", "message": "No se pudo obtener datos del CRS"}

    # 2️⃣ Guardar en la base de datos
    result = save_crs_data_to_db(db, data)

    return {
        "status": "ok",
        "journal_id": result["journal_id"],
        "transactions_inserted": result["transactions_inserted"]
    }
