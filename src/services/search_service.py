from src.utils.ontology_loader import load_ontology
from src.utils.url_parser import url_parser

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
            {
                "sujeto": url_parser(str(row.s)),
                "predicado": url_parser(str(row.p)),
                "objeto": url_parser(str(row.o)),
            }
        )
    return results
