from rest_framework import serializers

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

    def get_geom_wkt(self, obj):
        if obj.geom is None:
            return None
        return obj.geom.wkt

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