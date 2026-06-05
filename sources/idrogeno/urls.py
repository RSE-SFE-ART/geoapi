from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PozziViewSet, get_stratigrafia_by_pozzo, get_nearest_pozzi, get_pozzi_in_geometry

router = DefaultRouter()
router.register("pozzi", PozziViewSet, basename="pozzi")

urlpatterns = [
    path(
        "pozzi/in-geometry/",
        get_pozzi_in_geometry,
        name="pozzi-in-geometry",
    ),
    path(
        "pozzi/nearest/",
        get_nearest_pozzi,
        name="pozzi-nearest",
    ),
    path(
        "pozzi/<int:id_pozzo>/stratigrafia/",
        get_stratigrafia_by_pozzo,
        name="pozzo-stratigrafia",
    ),
]

urlpatterns += router.urls