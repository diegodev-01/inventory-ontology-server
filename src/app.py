from fastapi import FastAPI
from src.routes import search_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ontology Search API", version="1.0.0")

app.include_router(search_router.router, prefix="/api", tags=["search"])

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://inventory-ontology-web.pages.dev/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
