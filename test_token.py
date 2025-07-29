import asyncio
from app.crs.auth import get_token

async def main():
    token = await get_token()
    print(f"🔑 Token obtenido: {token}")

asyncio.run(main())
