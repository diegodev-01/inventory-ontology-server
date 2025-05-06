from rdflib import Graph
from pathlib import Path


def load_ontology(file_path: str = None) -> Graph:
    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / "../data/ontology.rdf"
        file_path = file_path.resolve()

    g = Graph()
    g.parse(str(file_path), format="xml")
    return g
