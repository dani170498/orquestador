import asyncio
import datetime
import httpx, json, datetime
from crs.auth import get_token

async def get_crs_data(location_id: int, start_date: str, end_date: str):
    token, _ = await get_token()

    url = (
        "https://crspruebas.mariestopes.org.bo/apimsbolivia/public/api/contabilidad"
        f"?access_token={token}&LOCATION_LID={location_id}&START_DATE={start_date}&END_DATE={end_date}"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers={"Authorization": f"Bearer {token}"})

        if response.status_code == 200:
            data = response.json()

            # Guardar copia local del JSON (opcional)
            fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            with open(f"data_{fecha}.json", "w") as f:
                json.dump(data, f, indent=2)

            return data
        else:
            return None