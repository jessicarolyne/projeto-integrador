# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

from rest_framework import routers
from app.api import viwsets as cadmapsviewsets

route = routers.DefaultRouter()
route.register(r'mapeamento',cadmapsviewsets.CadMapViewSet,basename="Cad_Mapeamento")
route.register(r'setores',cadmapsviewsets.CadSetoresViewSet,basename="Cad_setores")
route.register(r'equipes',cadmapsviewsets.CadEquipesViewSet,basename="Cad_equipes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this
    path("api/", include(route.urls))
]
