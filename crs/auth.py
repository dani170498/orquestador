import httpx
import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.token_api import TokenAPI
from app.core.database import SessionLocal

async def get_token():
    """
    Obtiene el token del CRS desde la BD.
    Si no existe o expiró, solicita uno nuevo y lo guarda.
    """
    db: Session = SessionLocal()

    # 1️⃣ Buscar token existente para "CRS"
    token_db = db.execute(
        select(TokenAPI).where(TokenAPI.sistema == "CRS")
    ).scalars().first()

    if token_db and token_db.expiracion > datetime.datetime.now():
        db.close()
        return token_db.token

    # 2️⃣ Si no hay token válido, pedimos uno nuevo
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://crspruebas.mariestopes.org.bo/apimsbolivia/public/oauth/access_token",
            data={
                "grant_type": "client_credentials",
                "client_id": 5,
                "client_secret": "31YHJ3gWDWoBkhdlEcfTJzivnfpoxd4vmrjI9bel"
            }
        )
        response.raise_for_status()
        data = response.json()

    nuevo_token = data["access_token"]
    expiracion = datetime.datetime.now() + datetime.timedelta(seconds=data.get("expires_in", 86400))

    # 3️⃣ Guardamos o actualizamos en BD
    if token_db:
        token_db.token = nuevo_token
        token_db.expiracion = expiracion
    else:
        token_db = TokenAPI(sistema="CRS", token=nuevo_token, expiracion=expiracion)
        db.add(token_db)

    db.commit()
    db.close()

    print(f"🔑 Nuevo token CRS guardado en BD: {nuevo_token}")
    return nuevo_token
