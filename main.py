from fastapi import FastAPI
import uvicorn
from app.api import ping  # Importá los routers que vayas creando
from app.api import routes, journal_routes # Importa las rutas que has definido

app = FastAPI(
    title="Orquestador de Procesos",
    version="1.0.0"
)

# Montar rutas
app.include_router(ping.router)
app.include_router(routes.router)  # Asegúrate de que 'routes' es el nombre correcto del archivo
app.include_router(journal_routes.router)  # Asegúrate de que 'journal_routes' es el nombre correcto del archivo
@app.get("/")
async def read_root():
    return {"message": "Hola mi nombre es Daniel!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
