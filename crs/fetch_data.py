import json
from auth import get_token
import httpx
import asyncio
import datetime
async def get_crs_data():
    TOKEN = await get_token()
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://crspruebas.mariestopes.org.bo/apimsbolivia/public/api/contabilidad?access_token={TOKEN}&LOCATION_LID=1&START_DATE=14/07/2025&END_DATE=15/07/2025",
            headers={"Authorization": f"Bearer {TOKEN}"}
        )
        # Imprimir el token utilizado
        print(f"Token utilizado: {TOKEN}")
        # Imprimir la URL de la solicitud
        print(f"URL de la solicitud: {response.url}")
        # Verificamos si la respuesta fue exitosa
        if response.status_code == 200:
            data = response.json()

            # Imprimir el JSON en consola, con formato legible
            print(json.dumps(data, indent=2))

            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Guardarlo en un archivo
            with open(f"data_{fecha_actual}.json", "w") as f:
                json.dump(data, f, indent=2)

            return data
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
        
#PROCESO MAIN
if __name__ == "__main__":
    asyncio.run(get_crs_data())