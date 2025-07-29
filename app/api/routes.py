from fastapi import APIRouter
from crs.auth import get_token

router = APIRouter()

@router.get("/crs/token")
async def get_crs_token():
    token = await get_token()
    return {"token": token}
