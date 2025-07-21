import httpx
import datetime
import asyncio

TOKEN = None
TOKEN_EXPIRATION = None

async def get_token():
    global TOKEN, TOKEN_EXPIRATION
    if TOKEN is None or datetime.datetime.now() >= TOKEN_EXPIRATION:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://crspruebas.mariestopes.org.bo/apimsbolivia/public/oauth/access_token",
                data={
                    "grant_type": "client_credentials",
                    "client_id": 5,
                    "client_secret": "31YHJ3gWDWoBkhdlEcfTJzivnfpoxd4vmrjI9bel"
                }
            )
            response_data = response.json()
            TOKEN = response_data.get("access_token")
            print(f"Token obtenido: {TOKEN}")
            expires_in = response_data.get("expires_in", 86400)
            TOKEN_EXPIRATION = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
    return TOKEN

# Ejecuta el token
if __name__ == "__main__":
    asyncio.run(get_token())
