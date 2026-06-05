from django.contrib.gis import admin

from .models import AnagraficaPozzi


@admin.register(AnagraficaPozzi)
class AnagraficaPozziAdmin(admin.GISModelAdmin):
    using = "dbeta"

    list_display = (
        "id_pozzo",
        "nome_pozzo",
        "regione",
        "provincia",
        "ub",
        "data",
    )

    search_fields = (
        "id_pozzo",
        "nome_pozzo",
        "regione",
        "provincia",
        "ub",
    )

    list_filter = (
        "regione",
        "provincia",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def has_delete_permission(self, request, obj=None):
        return False