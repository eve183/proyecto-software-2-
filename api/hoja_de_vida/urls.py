from django.urls import path

from .views import (
    listar_hojas_de_vida,
    obtener_hoja_de_vida
)


urlpatterns = [
    path('', listar_hojas_de_vida, name='listar_hojas_de_vida'),
    path('<int:id>/', obtener_hoja_de_vida, name='obtener_hoja_de_vida'),
]