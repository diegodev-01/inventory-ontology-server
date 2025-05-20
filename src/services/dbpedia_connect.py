from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD
from SPARQLWrapper import SPARQLWrapper, JSON
from datetime import datetime

INVENTORY = Namespace("http://www.semanticweb.org/usuario/ontologies/2025/2/Inventory#")
DBO = Namespace("http://dbpedia.org/ontology/")


def fetch_warehouses(limit=5):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    sparql.setQuery(f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?warehouse ?label WHERE {{
        ?warehouse rdfs:label ?label .
        FILTER (lang(?label) = "en" && CONTAINS(LCASE(?label), "warehouse"))
    }} LIMIT {limit}
    """)
    results = sparql.query().convert()
    return results["results"]["bindings"]


def populate_inventory_ontology(g: Graph) -> int:
    g.bind("inv", INVENTORY)
    warehouses = fetch_warehouses()

    for w in warehouses:
        print(w)
        almacen_uri = URIRef(w["warehouse"]["value"])
        label = Literal(w["label"]["value"], lang="en")

        # Almacen
        g.add((almacen_uri, RDF.type, INVENTORY.Almacen))
        g.add((almacen_uri, RDFS.label, label))

        # Existencias
        existencias_uri = URIRef(f"{almacen_uri}/existencias")
        g.add((existencias_uri, RDF.type, INVENTORY.Existencias))
        g.add((existencias_uri, INVENTORY.cantidad, Literal(100, datatype=XSD.integer)))
        g.add(
            (almacen_uri, INVENTORY.tieneExistencias, existencias_uri)
        )

        # Historial
        historial_uri = URIRef(f"{almacen_uri}/historial")
        g.add((historial_uri, RDF.type, INVENTORY.Historial))
        g.add(
            (
                historial_uri,
                INVENTORY.fecha,
                Literal(datetime.now().isoformat(), datatype=XSD.dateTime),
            )
        )
        g.add(
            (
                historial_uri,
                INVENTORY.descripcion,
                Literal("Ingreso inicial de inventario."),
            )
        )
        g.add(
            (almacen_uri, INVENTORY.tieneHistorial, historial_uri)
        )

    return len(warehouses)
