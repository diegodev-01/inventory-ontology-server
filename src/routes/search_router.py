from fastapi import APIRouter, Query
from src.services.search_service import search_ontology_by_label

router = APIRouter()


@router.get("/search")
def search_ontology(query: str = Query(..., description="Search term")):
    results = search_ontology_by_label(query)
    return {"results": results}
