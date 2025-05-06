from src.utils.ontology_loader import load_ontology

g = load_ontology()


def search_ontology_by_label(query: str):
    query_lower = query.lower()
    sparql = f"""
    SELECT ?s ?p ?o WHERE {{
        ?s ?p ?o .
        FILTER (
            CONTAINS(LCASE(STR(?s)), "{query_lower}") ||
            CONTAINS(LCASE(STR(?p)), "{query_lower}") ||
            CONTAINS(LCASE(STR(?o)), "{query_lower}")
        )
    }}
    LIMIT 50
    """
    results = []

    for row in g.query(sparql):
        results.append(
            {"sujeto": str(row.s), "predicado": str(row.p), "objeto": str(row.o)}
        )
    return results
