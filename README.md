# Inventory-ontology-server

Este es un servidor backend construido con **FastAPI** y **Python**, diseñado para exponer una ontología (en formato RDF/OWL) a través de una API REST. Sigue una estructura basada en **Clean Architecture** para asegurar mantenibilidad, escalabilidad y separación de responsabilidades.

## Características principales

- Backend moderno con FastAPI
- Estructura limpia (Clean Architecture)
- Consultas SPARQL a ontologías RDF/OWL usando `rdflib`
- Ontología local en formato RDF/XML
- Hot reload para desarrollo

## Estructura del Proyecto

``` markdown
inventory-ontology-server/
├── main.py              # Punto de entrada que expone la app desde src/
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Documentación del proyecto
└── src/
    ├── config/          # Configuraciones generales
    ├── controllers/     # Endpoints (routers de FastAPI)
    ├── routes/          # Agrupación de routers
    ├── services/        # Casos de uso / lógica de negocio
    ├── models/          # Modelos Pydantic y entidades de dominio
    ├── utils/           # Lectura de RDF, helpers, SPARQL, etc.
    └── app.py           # Inicializa FastAPI e incluye los routers
```

## Requisitos

- Python 3.12.6 o superior
- `pip` o `poetry` para instalar dependencias

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/inventory-ontology-server.git
cd inventory-ontology-server

# Crear entorno virtual (si no tienen esto, se les instalarán las dependencias globalmente)
python -m venv venv
# En Linux
source venv/bin/activate
# En Windows
venv\Scripts\activate en Windows
# En terminales Unix en Windows
source venv/Scripts/activate

# Instalar dependencias
pip install -r requirements.txt

```

## Ejecutar el servidor

Opción 1 - Usando univorn directamente

``` bash
uvicorn main:app --reload
```

Opción 2 - Usando la CLI de FastAPI

``` bash
fastapi dev main.py
```

## Formato de la Ontología

La ontología debe estar ubicada en:

``` bash
src/data/ontología.rdf
```

Ejemplo de Endpoint

``` bash
GET /buscar?query=existencia
```

devuelve una lista de existencias de la ontologia que sean existencias del almacen

{
  "resultados": [
    {
      "uri": "http://example.org/ontology#Existencia",
      "name": "Item001"
    },
    {
      "uri": "http://example.org/ontology#Existencia",
      "name": "Item002"
    },
    {
      "uri": "http://example.org/ontology#Existencia",
      "name": "Item003"
    }
  ]
}
