from src.utils.ontology_loader import load_ontology
from src.utils.url_parser import url_parser

def search_ontology_by_label(query: str, path: str = "../data/ontology.rdf", lang_code: str = "es"):
    g = load_ontology(file_path=path)
    query_lower = query.lower()

    sparql = f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?s ?sLabel ?p ?pLabel ?o ?oLabel WHERE {{
        ?s ?p ?o .

        OPTIONAL {{
            ?s rdfs:label ?sLabel .
            FILTER (lang(?sLabel) = "{lang_code}")
        }}
        OPTIONAL {{
            ?p rdfs:label ?pLabel .
            FILTER (lang(?pLabel) = "{lang_code}")
        }}
        OPTIONAL {{
            ?o rdfs:label ?oLabel .
            FILTER (lang(?oLabel) = "{lang_code}")
        }}

        FILTER (
            CONTAINS(LCASE(STR(?s)), "{query_lower}") ||
            CONTAINS(LCASE(STR(?p)), "{query_lower}") ||
            CONTAINS(LCASE(STR(?o)), "{query_lower}") ||
            CONTAINS(LCASE(STR(?sLabel)), "{query_lower}") ||
            CONTAINS(LCASE(STR(?pLabel)), "{query_lower}") ||
            CONTAINS(LCASE(STR(?oLabel)), "{query_lower}")
        )
    }}
    LIMIT 50
    """

    results = []
    for row in g.query(sparql):
        results.append(
            {
                "sujeto": url_parser(str(row["s"])),
                "sujeto_label": str(row["sLabel"]) if row.get("sLabel") else None,
                "predicado": url_parser(str(row["p"])),
                "predicado_label": str(row["pLabel"]) if row.get("pLabel") else None,
                "objeto": url_parser(str(row["o"])),
                "objeto_label": str(row["oLabel"]) if row.get("oLabel") else None,
            }
        )

    return results
