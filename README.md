# geoapi

# GeoAPI

GeoAPI is a prototype Django REST API for querying geospatial data from PostGIS databases.

The project is part of the work described in **“Towards a modular and open API for interoperable energy WebGIS platforms”**, focused on building a modular and programmatic access layer for geospatial datasets used in energy planning and WebGIS workflows.

The current prototype starts from the `idrogeno` schema and exposes selected data through REST endpoints.

## Current features

* Read-only API for `pozzi`
* Detail endpoint for a single `pozzo`
* Stratigraphy endpoint for a selected `pozzo`
* Spatial query for nearest `pozzi` to a point
* Spatial query for `pozzi` inside a geometry
* Example notebook showing how to use the API in automated workflows

## Example endpoints

```text
GET  /api/idrogeno/pozzi/
GET  /api/idrogeno/pozzi/{id_pozzo}/
GET  /api/idrogeno/pozzi/{id_pozzo}/stratigrafia/

POST /api/idrogeno/pozzi/nearest/
POST /api/idrogeno/pozzi/in-geometry/
```

## API documentation

When the development server is running, API documentation is available at:

```text
/api/docs/
```

## Example notebook

An example notebook is included in the repository to show how the existing endpoints can be used in an automated workflow.

The notebook demonstrates examples such as:

* finding the closest `pozzi` to a point;
* selecting `pozzi` inside an area;
* retrieving the `stratigrafia` for selected `pozzi`;


## Notes

This is currently a prototype and exposes only a representative subset of the available geospatial data infrastructure.

The project is designed to grow modularly, adding more schemas, datasets, spatial queries and processing services over time.
