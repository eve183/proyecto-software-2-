from django.urls import path

from .views import (
    listar_postulaciones,
    obtener_postulacion
)


urlpatterns = [
    path('', listar_postulaciones, name='listar_postulaciones'),
    path('<int:id>/', obtener_postulacion, name='obtener_postulacion'),
]