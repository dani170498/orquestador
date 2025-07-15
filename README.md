## Estructura de carpetas y para que son

orquestador/
├── app/                         # Código principal de la app
│   ├── api/                     # Lógica de consumo de APIs externas
│   ├── core/                    # Config global, DB, logging, errores
│   ├── db/                      # Modelos y acceso a la base de datos
│   ├── services/                # Lógica propia del orquestador (mapeo, validación, reglas)
│   ├── schemas/                 # Validaciones con Pydantic
│   ├── ui/                      # Código de interfaz visual (opcional: streamlit o fastapi frontend)
│   └── utils/                   # Funciones utilitarias reutilizables
├── tests/                       # Tests automáticos
├── .env                         # Variables de entorno
├── .gitignore                   # Archivos que no subís al repo
├── requirements.txt             # Dependencias del proyecto
├── Dockerfile                   # (opcional) para contenerizar
├── docker-compose.yml           # (opcional) para PostgreSQL + FastAPI + pgAdmin
├── alembic/                     # (opcional) migraciones de BD si usás Alembic
├── README.md                    # Documentación básica
└── main.py                      # Punto de entrada principal (levanta la app)
