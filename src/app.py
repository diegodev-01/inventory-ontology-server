from fastapi import FastAPI
from src.routes import search_router

app = FastAPI(title="Ontology Search API", version="1.0.0")

app.include_router(search_router.router, prefix="/api", tags=["search"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
