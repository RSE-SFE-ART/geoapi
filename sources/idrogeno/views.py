# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

import json

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr
from rest_framework import status

from .models import AnagraficaPozzi, Stratigrafia
from .serializers import AnagraficaPozziSerializer, StratigrafiaSerializer


class PozziViewSet(ReadOnlyModelViewSet):
    serializer_class = AnagraficaPozziSerializer
    lookup_field = "id_pozzo"

    def get_queryset(self):
        queryset = AnagraficaPozzi.objects.using("dbeta").all()

        regione = self.request.query_params.get("regione")
        provincia = self.request.query_params.get("provincia")

        if regione:
            queryset = queryset.filter(regione__iexact=regione)

        if provincia:
            queryset = queryset.filter(provincia__iexact=provincia)

        return queryset
    
@api_view(["GET"])
def get_stratigrafia_by_pozzo(request, id_pozzo):
    pozzo_exists = (
        AnagraficaPozzi.objects.using("dbeta")
        .filter(id_pozzo=id_pozzo)
        .exists()
    )

    if not pozzo_exists:
        return Response(
            {
                "id_pozzo": id_pozzo,
                "message": f"Pozzo {id_pozzo} does not exist.",
            },
            status=404,
        )

    rows = (
        Stratigrafia.objects.using("dbeta")
        .filter(id_pozzo=id_pozzo)
        .order_by("profondita_min")
    )

    if not rows.exists():
        return Response(
            {
                "id_pozzo": id_pozzo,
                "results": [],
                "message": f"Pozzo {id_pozzo} exists, but has no stratigrafia.",
            }
        )

    serializer = StratigrafiaSerializer(rows, many=True)

    return Response(
        {
            "id_pozzo": id_pozzo,
            "count": rows.count(),
            "results": serializer.data,
        }
    )

@api_view(["POST"])
def get_nearest_pozzi(request):
    srid = request.data.get("srid")
    geometry = request.data.get("geometry")
    n = request.data.get("n", 1)

    if srid is None:
        return Response(
            {"detail": "Missing required field: srid."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if geometry is None:
        return Response(
            {"detail": "Missing required field: geometry."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        srid = int(srid)
        n = int(n)
    except ValueError:
        return Response(
            {"detail": "srid and n must be integers."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if n < 1:
        return Response(
            {"detail": "n must be greater than or equal to 1."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        input_geom = fromstr(json.dumps(geometry))
        input_geom.srid = srid
    except Exception as exc:
        return Response(
            {
                "detail": "Invalid geometry. Expected GeoJSON geometry.",
                "error": str(exc),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if input_geom.geom_type != "Point":
        return Response(
            {"detail": "Geometry must be a Point."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # anagrafica_pozzi.geom is EPSG:32632
    if input_geom.srid != 32632:
        input_geom.transform(32632)

    rows = (
        AnagraficaPozzi.objects.using("dbeta")
        .exclude(geom__isnull=True)
        .annotate(distance=Distance("geom", input_geom))
        .order_by("distance")[:n]
    )

    serializer = AnagraficaPozziSerializer(rows, many=True)

    results = []
    for obj, data in zip(rows, serializer.data):
        item = dict(data)
        item["distance_m"] = obj.distance.m
        results.append(item)


    return Response(
        {
            "query": {
                "srid": srid,
                "geometry": geometry,
                "n": n,
            },
            "target_srid": 32632,
            "count": len(serializer.data),
            "results": results,
        }
    )

@api_view(["POST"])
def get_pozzi_in_geometry(request):
    srid = request.data.get("srid")
    geometry = request.data.get("geometry")

    if srid is None:
        return Response(
            {"detail": "Missing required field: srid."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if geometry is None:
        return Response(
            {"detail": "Missing required field: geometry."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        srid = int(srid)
    except ValueError:
        return Response(
            {"detail": "srid must be an integer."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        input_geom = fromstr(json.dumps(geometry))
        input_geom.srid = srid
    except Exception as exc:
        return Response(
            {
                "detail": "Invalid geometry. Expected GeoJSON geometry.",
                "error": str(exc),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    allowed_types = [
        "Polygon",
        "MultiPolygon",
    ]

    if input_geom.geom_type not in allowed_types:
        return Response(
            {
                "detail": "Geometry must be a Polygon or MultiPolygon.",
                "received_type": input_geom.geom_type,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    # anagrafica_pozzi.geom is EPSG:32632
    if input_geom.srid != 32632:
        input_geom.transform(32632)

    rows = (
        AnagraficaPozzi.objects.using("dbeta")
        .exclude(geom__isnull=True)
        .filter(geom__intersects=input_geom)
        .order_by("id_pozzo")
    )

    serializer = AnagraficaPozziSerializer(rows, many=True)

    return Response(
        {
            "query": {
                "srid": srid,
                "geometry": geometry,
            },
            "target_srid": 32632,
            "count": len(serializer.data),
            "results": serializer.data,
        }
    )