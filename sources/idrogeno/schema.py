from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
)

from .serializers import (
    AnagraficaPozziSerializer,
    StratigrafiaByPozzoResponseSerializer,
    NearestPozziRequestSerializer,
    NearestPozziResponseSerializer,
    PozziInGeometryRequestSerializer,
    PozziInGeometryResponseSerializer,
)


pozzi_list_schema = extend_schema(
    tags=["Pozzi"],
    summary="List wells",
    description=(
        "Returns the list of wells from the idrogeno schema. "
        "The result can be filtered by region and/or province using query parameters."
    ),
    parameters=[
        OpenApiParameter(
            name="regione",
            description="Filter wells by region name.",
            required=False,
            type=str,
        ),
        OpenApiParameter(
            name="provincia",
            description="Filter wells by province name.",
            required=False,
            type=str,
        ),
    ],
    responses={200: AnagraficaPozziSerializer(many=True)},
)


pozzi_retrieve_schema = extend_schema(
    tags=["Pozzi"],
    summary="Get one well",
    description="Returns the details of a single well.",
    responses={200: AnagraficaPozziSerializer},
)


stratigrafia_by_pozzo_schema = extend_schema(
    tags=["Stratigrafia"],
    summary="Get stratigraphy for a well",
    description=(
        "Returns stratigraphy records associated with a given well identifier. "
        "Records are ordered by minimum depth."
    ),
    parameters=[
        OpenApiParameter(
            name="id_pozzo",
            description="Well identifier.",
            required=True,
            type=int,
            location=OpenApiParameter.PATH,
        )
    ],
    responses={
        200: StratigrafiaByPozzoResponseSerializer,
        404: OpenApiResponse(description="The requested well does not exist."),
    },
)


nearest_pozzi_schema = extend_schema(
    tags=["Spatial queries"],
    summary="Find nearest wells",
    description=(
        "Returns the nearest wells to an input GeoJSON Point.\n\n"
        "The input geometry is interpreted using the provided SRID. "
        "If the SRID differs from EPSG:32632, the geometry is transformed before querying.\n\n"
        "Distances are returned in meters."
    ),
    request=NearestPozziRequestSerializer,
    responses={
        200: NearestPozziResponseSerializer,
        400: OpenApiResponse(description="Invalid request body or invalid geometry."),
    },
    examples=[
        OpenApiExample(
            "Nearest well request",
            value={
                "srid": 32632,
                "geometry": {
                    "type": "Point",
                    "coordinates": [500000, 5050000],
                },
                "n": 1,
            },
            request_only=True,
        ),
        OpenApiExample(
            "Nearest five wells request",
            value={
                "srid": 32632,
                "geometry": {
                    "type": "Point",
                    "coordinates": [520000, 5060000],
                },
                "n": 5,
            },
            request_only=True,
        ),
    ],
)


pozzi_in_geometry_schema = extend_schema(
    tags=["Spatial queries"],
    summary="Find wells inside a geometry",
    description=(
        "Returns wells whose point geometry intersects the input GeoJSON Polygon "
        "or MultiPolygon.\n\n"
        "Use this endpoint for spatial selections where the input geometry is too "
        "complex or too long to pass as URL parameters."
    ),
    request=PozziInGeometryRequestSerializer,
    responses={
        200: PozziInGeometryResponseSerializer,
        400: OpenApiResponse(description="Invalid request body or invalid geometry."),
    },
    examples=[
        OpenApiExample(
            "Polygon selection request",
            value={
                "srid": 32632,
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [450000, 5000000],
                            [650000, 5000000],
                            [650000, 5200000],
                            [450000, 5200000],
                            [450000, 5000000],
                        ]
                    ],
                },
            },
            request_only=True,
        )
    ],
)