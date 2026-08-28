from django.urls import path

from .views import (
    listar_notificaciones,
    obtener_notificacion
)


urlpatterns = [
    path('', listar_notificaciones, name='listar_notificaciones'),
    path('<int:id>/', obtener_notificacion, name='obtener_notificacion'),
]