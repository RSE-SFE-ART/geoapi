# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    fid = models.BigIntegerField(blank=True, null=True)
    esperienza = models.CharField(max_length=10, blank=True, null=True)
    suggerimenti = models.CharField(max_length=10000, blank=True, null=True)
    consiglierebbe = models.CharField(max_length=10, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    sito_web = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_feedback'


class Abr(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=254, blank=True, null=True)
    osm_way_id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    aeroway = models.CharField(max_length=254, blank=True, null=True)
    amenity = models.CharField(max_length=254, blank=True, null=True)
    admin_leve = models.CharField(max_length=254, blank=True, null=True)
    barrier = models.CharField(max_length=254, blank=True, null=True)
    boundary = models.CharField(max_length=254, blank=True, null=True)
    building = models.CharField(max_length=254, blank=True, null=True)
    craft = models.CharField(max_length=254, blank=True, null=True)
    geological = models.CharField(max_length=254, blank=True, null=True)
    historic = models.CharField(max_length=254, blank=True, null=True)
    land_area = models.CharField(max_length=254, blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True)
    leisure = models.CharField(max_length=254, blank=True, null=True)
    man_made = models.CharField(max_length=254, blank=True, null=True)
    military = models.CharField(max_length=254, blank=True, null=True)
    natural = models.CharField(max_length=254, blank=True, null=True)
    office = models.CharField(max_length=254, blank=True, null=True)
    place = models.CharField(max_length=254, blank=True, null=True)
    shop = models.CharField(max_length=254, blank=True, null=True)
    sport = models.CharField(max_length=254, blank=True, null=True)
    tourism = models.CharField(max_length=254, blank=True, null=True)
    other_tags = models.CharField(max_length=254, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    perimeter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'abr'


class AnagraficaPozzi(models.Model):
    id_pozzo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    geom = models.PointField(srid=32632, blank=True, null=True)
    nome_pozzo = models.CharField(max_length=254, blank=True, null=True)
    ub = models.CharField(max_length=254, blank=True, null=True)
    regione = models.CharField(max_length=254, blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    x_32632 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    y_32632 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anagrafica_pozzi'


class AnagraficaPozziIdrici(models.Model):
    codice_isp = models.BigIntegerField(primary_key=True)
    geom = models.PointField(srid=32632, blank=True, null=True)
    x_utm32n = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    y_utm32n = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    regione = models.CharField(max_length=254, blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    comune = models.CharField(max_length=254, blank=True, null=True)
    opera = models.BigIntegerField(blank=True, null=True)
    profondita = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    udm_prof = models.BigIntegerField(blank=True, null=True)
    quota_pc = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    udm_quota = models.BigIntegerField(blank=True, null=True)
    anno = models.BigIntegerField(blank=True, null=True)
    n_diam = models.BigIntegerField(blank=True, null=True)
    acqua = models.CharField(max_length=254, blank=True, null=True)
    q_max = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    udm_q_max = models.BigIntegerField(blank=True, null=True)
    q_es = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    udm_q_es = models.BigIntegerField(blank=True, null=True)
    n_falde = models.BigIntegerField(blank=True, null=True)
    n_filtri = models.BigIntegerField(blank=True, null=True)
    n_piezomet = models.BigIntegerField(blank=True, null=True)
    stratigraf = models.CharField(max_length=254, blank=True, null=True)
    numero_str = models.BigIntegerField(db_column='numero str', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    webpage = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anagrafica_pozzi_idrici'


class Analisi(models.Model):
    id_analisi = models.IntegerField(blank=True, null=True)
    analisi = models.CharField(blank=True, null=True)
    descrizione_analisi = models.CharField(blank=True, null=True)
    udm = models.CharField(blank=True, null=True)
    id_udm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analisi'


class AnalisiChimiche(models.Model):
    id = models.IntegerField(primary_key=True)
    id_campione = models.CharField(blank=True, null=True)
    id_analisi = models.IntegerField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analisi_chimiche'


class AziendeAltoConsumo(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    id_input = models.BigIntegerField(blank=True, null=True)
    id_rse = models.BigIntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    long = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    settore_or = models.BigIntegerField(blank=True, null=True)
    settore = models.BigIntegerField(blank=True, null=True)
    regione = models.CharField(max_length=254, blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    comune = models.CharField(max_length=254, blank=True, null=True)
    codpro = models.BigIntegerField(blank=True, null=True)
    pro_com_t = models.BigIntegerField(blank=True, null=True)
    x = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    y = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'aziende_alto_consumo'


class Bas(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=254, blank=True, null=True)
    osm_way_id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    aeroway = models.CharField(max_length=254, blank=True, null=True)
    amenity = models.CharField(max_length=254, blank=True, null=True)
    admin_leve = models.CharField(max_length=254, blank=True, null=True)
    barrier = models.CharField(max_length=254, blank=True, null=True)
    boundary = models.CharField(max_length=254, blank=True, null=True)
    building = models.CharField(max_length=254, blank=True, null=True)
    craft = models.CharField(max_length=254, blank=True, null=True)
    geological = models.CharField(max_length=254, blank=True, null=True)
    historic = models.CharField(max_length=254, blank=True, null=True)
    land_area = models.CharField(max_length=254, blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True)
    leisure = models.CharField(max_length=254, blank=True, null=True)
    man_made = models.CharField(max_length=254, blank=True, null=True)
    military = models.CharField(max_length=254, blank=True, null=True)
    natural = models.CharField(max_length=254, blank=True, null=True)
    office = models.CharField(max_length=254, blank=True, null=True)
    place = models.CharField(max_length=254, blank=True, null=True)
    shop = models.CharField(max_length=254, blank=True, null=True)
    sport = models.CharField(max_length=254, blank=True, null=True)
    tourism = models.CharField(max_length=254, blank=True, null=True)
    other_tags = models.CharField(max_length=254, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    perimeter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'bas'


class Cal(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=254, blank=True, null=True)
    osm_way_id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    aeroway = models.CharField(max_length=254, blank=True, null=True)
    amenity = models.CharField(max_length=254, blank=True, null=True)
    admin_leve = models.CharField(max_length=254, blank=True, null=True)
    barrier = models.CharField(max_length=254, blank=True, null=True)
    boundary = models.CharField(max_length=254, blank=True, null=True)
    building = models.CharField(max_length=254, blank=True, null=True)
    craft = models.CharField(max_length=254, blank=True, null=True)
    geological = models.CharField(max_length=254, blank=True, null=True)
    historic = models.CharField(max_length=254, blank=True, null=True)
    land_area = models.CharField(max_length=254, blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True)
    leisure = models.CharField(max_length=254, blank=True, null=True)
    man_made = models.CharField(max_length=254, blank=True, null=True)
    military = models.CharField(max_length=254, blank=True, null=True)
    natural = models.CharField(max_length=254, blank=True, null=True)
    office = models.CharField(max_length=254, blank=True, null=True)
    place = models.CharField(max_length=254, blank=True, null=True)
    shop = models.CharField(max_length=254, blank=True, null=True)
    sport = models.CharField(max_length=254, blank=True, null=True)
    tourism = models.CharField(max_length=254, blank=True, null=True)
    other_tags = models.CharField(max_length=254, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    perimeter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cal'


class Cam(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=254, blank=True, null=True)
    osm_way_id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    aeroway = models.CharField(max_length=254, blank=True, null=True)
    amenity = models.CharField(max_length=254, blank=True, null=True)
    admin_leve = models.CharField(max_length=254, blank=True, null=True)
    barrier = models.CharField(max_length=254, blank=True, null=True)
    boundary = models.CharField(max_length=254, blank=True, null=True)
    building = models.CharField(max_length=254, blank=True, null=True)
    craft = models.CharField(max_length=254, blank=True, null=True)
    geological = models.CharField(max_length=254, blank=True, null=True)
    historic = models.CharField(max_length=254, blank=True, null=True)
    land_area = models.CharField(max_length=254, blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True)
    leisure = models.CharField(max_length=254, blank=True, null=True)
    man_made = models.CharField(max_length=254, blank=True, null=True)
    military = models.CharField(max_length=254, blank=True, null=True)
    natural = models.CharField(max_length=254, blank=True, null=True)
    office = models.CharField(max_length=254, blank=True, null=True)
    place = models.CharField(max_length=254, blank=True, null=True)
    shop = models.CharField(max_length=254, blank=True, null=True)
    sport = models.CharField(max_length=254, blank=True, null=True)
    tourism = models.CharField(max_length=254, blank=True, null=True)
    other_tags = models.CharField(max_length=254, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    perimeter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cam'


class Campione(models.Model):
    id_campione = models.CharField(primary_key=True)
    id_pozzo = models.CharField(blank=True, null=True)
    tipo_analisi = models.CharField(blank=True, null=True)
    mineralizzazione = models.CharField(blank=True, null=True)
    prof_min = models.CharField(blank=True, null=True)
    prof_max = models.CharField(blank=True, null=True)
    note = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campione'


class CanaliTematici(models.Model):
    id = models.IntegerField(primary_key=True)
    tematismo_it = models.CharField(db_column='tematismo_IT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tematismo_en = models.CharField(db_column='tematismo_EN', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'canali_tematici'
        db_table_comment = 'elenco dei canali tematici'


class Carote(models.Model):
    id_pozzo = models.IntegerField(blank=True, null=True)
    nome_pozzo = models.CharField(blank=True, null=True)
    prof_min = models.FloatField(blank=True, null=True)
    prof_max = models.FloatField(blank=True, null=True)
    tipo = models.CharField(blank=True, null=True)
    recupero_perc = models.FloatField(blank=True, null=True)
    eta = models.CharField(blank=True, null=True)
    formazione = models.CharField(blank=True, null=True)
    litologia = models.CharField(blank=True, null=True)
    carota_non_recuperata = models.CharField(blank=True, null=True)
    pend_min_gr = models.FloatField(blank=True, null=True)
    pend_max_gr = models.FloatField(blank=True, null=True)
    sigla_manifestazioni = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carote'


class Categorie(models.Model):
    id = models.IntegerField(primary_key=True)
    categoria_it = models.CharField(max_length=100, blank=True, null=True)
    categoria_en = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorie'
        db_table_comment = 'elenco categorie per ogni tematismo'


class CodLitologia(models.Model):
    cod_lit = models.IntegerField(primary_key=True)
    descrizione = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cod_litologia'


class CodOpera(models.Model):
    cod_opera = models.IntegerField(primary_key=True)
    descrizione = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cod_opera'


class CodRoccia(models.Model):
    cod_roccia = models.IntegerField(primary_key=True)
    descrizione = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cod_roccia'


class CodTipoTitoliMinerari(models.Model):
    cod_titolo = models.IntegerField(blank=True, null=True)
    descr_tipo_titolo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cod_tipo_titoli_minerari'


class CodTipoTitoliMinerariTotale(models.Model):
    cod_titolo_totale = models.IntegerField(blank=True, null=True)
    descr_tipo_titolo_totale = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cod_tipo_titoli_minerari_totale'


class ComNew(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    cod_rip = models.BigIntegerField(blank=True, null=True)
    cod_reg = models.BigIntegerField(blank=True, null=True)
    cod_prov = models.BigIntegerField(blank=True, null=True)
    cod_cm = models.BigIntegerField(blank=True, null=True)
    cod_uts = models.BigIntegerField(blank=True, null=True)
    pro_com = models.BigIntegerField(blank=True, null=True)
    pro_com_t = models.CharField(max_length=6, blank=True, null=True)
    comune = models.CharField(max_length=100, blank=True, null=True)
    comune_a = models.CharField(max_length=100, blank=True, null=True)
    cc_uts = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_le_1 = models.FloatField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    id_metadato = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_new'


class Comuni(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    gid = models.IntegerField(blank=True, null=True)
    cod_rip = models.FloatField(blank=True, null=True)
    cod_reg = models.FloatField(blank=True, null=True)
    cod_prov = models.FloatField(blank=True, null=True)
    pro_com = models.FloatField(blank=True, null=True)
    pro_com_t = models.CharField(max_length=6, blank=True, null=True)
    comune = models.CharField(max_length=100, blank=True, null=True)
    comune_a = models.CharField(max_length=100, blank=True, null=True)
    cc_uts = models.IntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    cod_cm = models.FloatField(blank=True, null=True)
    cod_uts = models.FloatField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    id_metadato = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuni'


class Esito(models.Model):
    cod_esito = models.CharField(blank=True, null=True)
    esito_i = models.CharField(blank=True, null=True)
    esito_e = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'esito'


class FeedbackNew(models.Model):
    id = models.IntegerField(primary_key=True)
    fid = models.BigIntegerField(blank=True, null=True)
    esperienza = models.CharField(max_length=10, blank=True, null=True)
    suggerimenti = models.CharField(max_length=10000, blank=True, null=True)
    consiglierebbe = models.CharField(max_length=10, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    sito_web = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_new'


class IdrogenoTesttable(models.Model):
    id_pozzo = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    geom = models.PointField(srid=32632, blank=True, null=True)
    nome_pozzo = models.CharField(max_length=254, blank=True, null=True)
    regione = models.CharField(max_length=254, blank=True, null=True)
    n_campione = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idrogeno_testtable'


class LinkMetadatoVariabili(models.Model):
    id = models.IntegerField(primary_key=True)
    id_metadato = models.IntegerField(blank=True, null=True)
    id_variabile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_metadato_variabili'


class LinkVariabiliCategorie(models.Model):
    id_variabile = models.IntegerField(blank=True, null=True)
    id_categoria = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'link_variabili_categorie'


class LinkVariabiliTematismi(models.Model):
    id_variabile = models.IntegerField(blank=True, null=True)
    id_tematismo = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'link_variabili_tematismi'


class LivelliUtente(models.Model):
    id = models.IntegerField(primary_key=True)
    utente = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    livello = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livelli_utente'
        db_table_comment = 'tabella utenti con livello di accesso ai dati'


class LomEstratto(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=254, blank=True, null=True)
    osm_way_id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    aeroway = models.CharField(max_length=254, blank=True, null=True)
    amenity = models.CharField(max_length=254, blank=True, null=True)
    admin_leve = models.CharField(max_length=254, blank=True, null=True)
    barrier = models.CharField(max_length=254, blank=True, null=True)
    boundary = models.CharField(max_length=254, blank=True, null=True)
    building = models.CharField(max_length=254, blank=True, null=True)
    craft = models.CharField(max_length=254, blank=True, null=True)
    geological = models.CharField(max_length=254, blank=True, null=True)
    historic = models.CharField(max_length=254, blank=True, null=True)
    land_area = models.CharField(max_length=254, blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True)
    leisure = models.CharField(max_length=254, blank=True, null=True)
    man_made = models.CharField(max_length=254, blank=True, null=True)
    military = models.CharField(max_length=254, blank=True, null=True)
    natural = models.CharField(max_length=254, blank=True, null=True)
    office = models.CharField(max_length=254, blank=True, null=True)
    place = models.CharField(max_length=254, blank=True, null=True)
    shop = models.CharField(max_length=254, blank=True, null=True)
    sport = models.CharField(max_length=254, blank=True, null=True)
    tourism = models.CharField(max_length=254, blank=True, null=True)
    other_tags = models.CharField(max_length=254, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    perimeter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'lom_estratto'


class Manifestazioni(models.Model):
    id_pozzo = models.IntegerField(blank=True, null=True)
    nome_pozzo = models.CharField(blank=True, null=True)
    prof_min = models.FloatField(blank=True, null=True)
    prof_max = models.FloatField(blank=True, null=True)
    codice = models.CharField(blank=True, null=True)
    tipo = models.CharField(blank=True, null=True)
    note = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifestazioni'


class MarneIsocroneZonab(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiLineStringField(srid=32632, dim=3, blank=True, null=True)
    twt = models.FloatField(blank=True, null=True)
    et_id = models.IntegerField(blank=True, null=True)
    et_source = models.CharField(max_length=200, blank=True, null=True)
    twt_msec = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marne_isocrone_zonab'


class Metadati(models.Model):
    id = models.IntegerField(primary_key=True)
    fonte_dato = models.CharField(blank=True, null=True)
    anno_riferimento = models.IntegerField(blank=True, null=True)
    formato = models.CharField(blank=True, null=True)
    standard = models.CharField(blank=True, null=True)
    link_metadato = models.CharField(blank=True, null=True)
    keywords = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadati'


class Mil(models.Model):

    class Meta:
        managed = False
        db_table = 'mil'


class Minerale(models.Model):
    cod_minerale = models.CharField(primary_key=True)
    descr_minerale = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minerale'


class NewTableName(models.Model):
    id_pozzo = models.CharField(blank=True, null=True)
    geom = models.PointField(srid=32632, blank=True, null=True)
    nome_pozzo = models.CharField(max_length=254, blank=True, null=True)
    regione = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_table_name'


class ParametriCaratteristici(models.Model):
    id_pozzo = models.BigIntegerField(blank=True, null=True)
    id_parametro = models.BigIntegerField(blank=True, null=True)
    profondita_min = models.BigIntegerField(blank=True, null=True)
    profondita_max = models.BigIntegerField(blank=True, null=True)
    valore_min = models.FloatField(blank=True, null=True)
    valore_max = models.FloatField(blank=True, null=True)
    unita_misura = models.CharField(blank=True, null=True)
    tipo_valore = models.CharField(blank=True, null=True)
    parametro = models.CharField(blank=True, null=True)
    note = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametri_caratteristici'


class PointcloudFormats(models.Model):
    pcid = models.IntegerField(primary_key=True)
    srid = models.IntegerField(blank=True, null=True)
    schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pointcloud_formats'


class PozziIdriciStratigrafia(models.Model):
    codice_ispra = models.BigIntegerField(blank=True, null=True)
    id_stratigrafia = models.IntegerField(blank=True, null=True)
    prof_min = models.FloatField(blank=True, null=True)
    prof_max = models.FloatField(blank=True, null=True)
    spessore = models.FloatField(blank=True, null=True)
    descr_litologica = models.CharField(blank=True, null=True)
    falda = models.CharField(blank=True, null=True)
    classe_litologica = models.IntegerField(blank=True, null=True)
    cond_term_dry = models.FloatField(blank=True, null=True)
    cond_term_wet = models.FloatField(blank=True, null=True)
    pot_term_dry = models.IntegerField(blank=True, null=True)
    pot_term_wet = models.IntegerField(blank=True, null=True)
    tipo_roccia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pozzi_idrici_stratigrafia'


class Scopo(models.Model):
    cod_scopo = models.CharField(primary_key=True)
    scopo_i = models.CharField(blank=True, null=True)
    scopo_e = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scopo'


class SigleManifCarote(models.Model):
    codice = models.CharField(blank=True, null=True)
    elemento = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sigle_manif_carote'


class SigleParametriCaratteristici(models.Model):
    id_parametro = models.BigIntegerField(blank=True, null=True)
    parametro = models.CharField(db_column='Parametro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sigle_parametri_caratteristici'


class StatoPozzo(models.Model):
    stato_pozzo = models.CharField(primary_key=True)
    descr_stato = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stato_pozzo'


class Stazioni3857(models.Model):
    gid = models.IntegerField(primary_key=True)
    objectid = models.FloatField(blank=True, null=True)
    stazione = models.FloatField(blank=True, null=True)
    longitudin = models.FloatField(blank=True, null=True)
    latitudine = models.FloatField(blank=True, null=True)
    nomestazio = models.CharField(max_length=254, blank=True, null=True)
    data_inizi = models.CharField(max_length=10, blank=True, null=True)
    data_fine = models.CharField(max_length=10, blank=True, null=True)
    perc_dati_field = models.FloatField(db_column='perc_dati_', blank=True, null=True)  # Field renamed because it ended with '_'.
    dati_valid = models.FloatField(blank=True, null=True)
    dati_del_p = models.FloatField(blank=True, null=True)
    altezza_an = models.FloatField(blank=True, null=True)
    quota = models.FloatField(blank=True, null=True)
    orogr = models.CharField(max_length=254, blank=True, null=True)
    carter = models.CharField(max_length=254, blank=True, null=True)
    dist_punto = models.FloatField(blank=True, null=True)
    the_geom = models.PointField(srid=3857, blank=True, null=True)
    origine = models.CharField(max_length=10, blank=True, null=True)
    attiva = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stazioni3857'


class Stratigrafia(models.Model):
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
        db_table = 'stratigrafia'


class Temperature(models.Model):
    id_pozzo = models.IntegerField(blank=True, null=True)
    id_temperatura = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    prof_min = models.FloatField(blank=True, null=True)
    prof_max = models.FloatField(blank=True, null=True)
    litologia = models.CharField(blank=True, null=True)
    temp_min_c = models.FloatField(blank=True, null=True)
    temp_max_c = models.FloatField(blank=True, null=True)
    tipo_valore = models.CharField(blank=True, null=True)
    tempo_h = models.IntegerField(blank=True, null=True)
    fonte = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temperature'


class Tempp(models.Model):
    id_pozzo = models.CharField(blank=True, null=True)
    geom = models.PointField(srid=32632, blank=True, null=True)
    nome_pozzo = models.CharField(max_length=254, blank=True, null=True)
    regione = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempp'


class Temppp(models.Model):
    id_pozzo = models.CharField(blank=True, null=True)
    geom = models.PointField(srid=32632, blank=True, null=True)
    nome_pozzo = models.CharField(max_length=254, blank=True, null=True)
    regione = models.CharField(max_length=254, blank=True, null=True)
    tipo_pozzo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temppp'


class TipoPozzo(models.Model):
    id_tipo_pozzo = models.BigIntegerField(primary_key=True)
    desc_tipo_pozzo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_pozzo'


class TipoTabella(models.Model):
    id = models.IntegerField(primary_key=True)
    descrizione = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_tabella'


class Tipologia(models.Model):
    id_pozzo = models.BigIntegerField(blank=True, null=True)
    id_tipologia = models.BigIntegerField(blank=True, null=True)
    sezione = models.CharField(blank=True, null=True)
    tipo_pozzo = models.CharField(blank=True, null=True)
    id_tipo_pozzo = models.BigIntegerField(blank=True, null=True)
    stato = models.CharField(blank=True, null=True)
    anno = models.BigIntegerField(blank=True, null=True)
    profondita = models.BigIntegerField(blank=True, null=True)
    nome_titolo = models.CharField(blank=True, null=True)
    tipo_titolo = models.CharField(blank=True, null=True)
    campo = models.CharField(blank=True, null=True)
    centrale = models.CharField(blank=True, null=True)
    piattaforma = models.CharField(blank=True, null=True)
    operatore = models.CharField(blank=True, null=True)
    minerale = models.CharField(blank=True, null=True)
    scopo = models.CharField(blank=True, null=True)
    esito = models.CharField(blank=True, null=True)
    disp = models.CharField(blank=True, null=True)
    pdf = models.CharField(blank=True, null=True)
    data_agg = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipologia'


class TipologiaUtente(models.Model):
    id = models.IntegerField(primary_key=True)
    settore = models.CharField(blank=True, null=True)
    ambito = models.CharField(max_length=900, blank=True, null=True)
    utilizzo = models.CharField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    note = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipologia_utente'


class TitoliMinerari(models.Model):
    id_titolo = models.IntegerField(blank=True, null=True)
    tipo_titolo = models.IntegerField(blank=True, null=True)
    tipo_titolo_totale = models.IntegerField(blank=True, null=True)
    nome = models.CharField(blank=True, null=True)
    richiedenti = models.CharField(blank=True, null=True)
    conferimento = models.CharField(blank=True, null=True)
    sospensione = models.CharField(blank=True, null=True)
    presentazione = models.CharField(blank=True, null=True)
    fase = models.CharField(blank=True, null=True)
    ub = models.CharField(blank=True, null=True)
    regione = models.CharField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    iter = models.CharField(blank=True, null=True)
    note = models.CharField(blank=True, null=True)
    aggiornamento = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titoli_minerari'


class Titolo(models.Model):
    cod_titolo = models.CharField(blank=True, null=True)
    tipo_titolo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titolo'


class Ubicazione(models.Model):
    cod_ub = models.CharField(primary_key=True)
    descr_ub = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicazione'


class Udm(models.Model):
    id_campo = models.IntegerField(primary_key=True)
    nome_campo = models.CharField(blank=True, null=True)
    udm = models.CharField(blank=True, null=True)
    descrizione = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'udm'


class UsoSuoloLivello1(models.Model):
    id = models.IntegerField(primary_key=True)
    livello = models.IntegerField(blank=True, null=True)
    descrizione = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uso_suolo_livello_1'


class UsoSuoloLivello2(models.Model):
    id = models.IntegerField(primary_key=True)
    livello1 = models.IntegerField(blank=True, null=True)
    livello2 = models.IntegerField(blank=True, null=True)
    descrizione = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uso_suolo_livello_2'


class UsoSuoloLivello3(models.Model):
    id = models.IntegerField(primary_key=True)
    livello1 = models.IntegerField(blank=True, null=True)
    livello2 = models.IntegerField(blank=True, null=True)
    livello3 = models.IntegerField(blank=True, null=True)
    descrizione = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uso_suolo_livello_3'


class Variabili(models.Model):
    id = models.IntegerField(primary_key=True)
    variabile = models.CharField(blank=True, null=True, db_comment='nome campo tabella variabili amministrative oppure nome tabella')
    descrizione_it = models.CharField(blank=True, null=True, db_comment='descrizione contenuto')
    udm_id = models.IntegerField(blank=True, null=True)
    tabella = models.CharField(max_length=200, blank=True, null=True, db_comment='nome dello schema e della tabella di appartenenza della variabile')
    livello_accesso = models.IntegerField(blank=True, null=True, db_comment='livello di accessibilità del dato:\n0 = accesso libero\n1 = solo elenco, dato non visibile e non scaricabile\n2 = dato non visibile')
    descrizione_en = models.CharField(max_length=500, blank=True, null=True)
    tipo_tabella = models.IntegerField(blank=True, null=True)
    servizio_geoserver = models.CharField(max_length=200, blank=True, null=True)
    temp_servizi = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variabili'
