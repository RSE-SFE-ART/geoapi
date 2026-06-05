from django.contrib.gis.db import models

# Create your models here.
class AnagraficaPozzi(models.Model):
    id_pozzo = models.FloatField(primary_key=True)
    geom = models.PointField(srid=32632, blank=True, null=True)
    nome_pozzo = models.CharField(max_length=254, blank=True, null=True)
    ub = models.CharField(max_length=254, blank=True, null=True)
    regione = models.CharField(max_length=254, blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    x_32632 = models.FloatField(blank=True, null=True)
    y_32632 = models.FloatField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"idrogeno"."anagrafica_pozzi"'
        verbose_name = "Anagrafica Pozzi"
        verbose_name_plural = "Anagrafica Pozzi"

    def __str__(self):
        return self.nome_pozzo
    
class Stratigrafia(models.Model):
    id = models.IntegerField(primary_key=True)
    id_pozzo = models.BigIntegerField(blank=True, null=True)
    profondita_min = models.BigIntegerField(blank=True, null=True)
    profondita_max = models.BigIntegerField(blank=True, null=True)
    eta = models.CharField(blank=True, null=True)
    formazione = models.CharField(blank=True, null=True)
    litologia = models.CharField(blank=True, null=True)
    note_litologia = models.CharField(blank=True, null=True)
    pendenza = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"idrogeno"."stratigrafia"'
        verbose_name = "Stratigrafia"
        verbose_name_plural = "Stratigrafie"

    def __str__(self):
        return f"Pozzo {self.id_pozzo}: stratigrafia {self.id} - {self.profondita_min}-{self.profondita_max}"