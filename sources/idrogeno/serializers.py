from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from .models import AnagraficaPozzi, Stratigrafia


class AnagraficaPozziSerializer(serializers.ModelSerializer):
    id_pozzo = serializers.CharField()
    x_32632 = serializers.FloatField(allow_null=True)
    y_32632 = serializers.FloatField(allow_null=True)
    geom_wkt = serializers.SerializerMethodField()

    class Meta:
        model = AnagraficaPozzi
        fields = [
            "id_pozzo",
            "nome_pozzo",
            "ub",
            "regione",
            "provincia",
            "x_32632",
            "y_32632",
            "data",
            "geom_wkt",
        ]

    @extend_schema_field({"type": "string", "nullable": True})
    def get_geom_wkt(self, obj):
        if obj.geom is None:
            return None
        return obj.geom.wkt


class NearestPozzoSerializer(AnagraficaPozziSerializer):
    distance_m = serializers.FloatField(
        help_text="Distance from the input point, in meters."
    )

    class Meta(AnagraficaPozziSerializer.Meta):
        fields = AnagraficaPozziSerializer.Meta.fields + ["distance_m"]


class StratigrafiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stratigrafia
        fields = [
            "id",
            "id_pozzo",
            "profondita_min",
            "profondita_max",
            "eta",
            "formazione",
            "litologia",
            "note_litologia",
            "pendenza",
        ]


class NearestPozziRequestSerializer(serializers.Serializer):
    srid = serializers.IntegerField(
        help_text="EPSG code of the input geometry. Example: 32632."
    )
    geometry = serializers.JSONField(
        help_text="GeoJSON Point geometry."
    )
    n = serializers.IntegerField(
        default=1,
        min_value=1,
        help_text="Maximum number of nearest wells to return."
    )


class PozziInGeometryRequestSerializer(serializers.Serializer):
    srid = serializers.IntegerField(
        help_text="EPSG code of the input geometry. Example: 32632."
    )
    geometry = serializers.JSONField(
        help_text="GeoJSON Polygon or MultiPolygon geometry."
    )


class NearestPozziResponseSerializer(serializers.Serializer):
    query = serializers.JSONField()
    target_srid = serializers.IntegerField()
    count = serializers.IntegerField()
    results = NearestPozzoSerializer(many=True)


class PozziInGeometryResponseSerializer(serializers.Serializer):
    query = serializers.JSONField()
    target_srid = serializers.IntegerField()
    count = serializers.IntegerField()
    results = AnagraficaPozziSerializer(many=True)


class StratigrafiaByPozzoResponseSerializer(serializers.Serializer):
    id_pozzo = serializers.CharField()
    count = serializers.IntegerField()
    results = StratigrafiaSerializer(many=True)