from fastapi import APIRouter, Query
from src.services.search_service import search_ontology_by_label
from pathlib import Path

from src.utils.ontology_loader import load_ontology
from src.services.dbpedia_connect import populate_inventory_ontology

router = APIRouter()

g = load_ontology()


@router.get("/search")
def search_ontology(query: str = Query(..., description="Search term")):
    results = search_ontology_by_label(query)
    return {"results": results}


@router.post("/add-dbpedia")
def add_dbpedia_data():
    g = load_ontology()
    try:
        populate_inventory_ontology(g)
        base_dir = Path(__file__).resolve().parent
        g.serialize(base_dir / "../data/ontology_poblada.rdf", format="xml")
        return {"message": "Ontology populated successfully."}
    except Exception as e:
        return {"error": str(e)}


@router.get("/search-db")
def search_dbpedia(query: str = Query(..., description="Search term")):
    results = search_ontology_by_label(query, path="../data/ontology_poblada.rdf")
    return {"results": results}
