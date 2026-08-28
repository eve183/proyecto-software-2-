import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Notificacion


@api_view(['GET'])
def listar_notificaciones(request):
    notificaciones = Notificacion.objects.all()

    datos = []

    for notificacion in notificaciones:
        datos.append({
            'id': notificacion.id,
            'destinatario': notificacion.destinatario,
            'mensaje': notificacion.mensaje,
            'fechaEnvio': notificacion.fechaEnvio,
            'enviada': notificacion.enviada,
            'usuario_id': notificacion.usuario_id
        })

    return Response(datos)


@api_view(['GET'])
def obtener_notificacion(request, id):
    try:
        notificacion = Notificacion.objects.get(id=id)

        datos = {
            'id': notificacion.id,
            'destinatario': notificacion.destinatario,
            'mensaje': notificacion.mensaje,
            'fechaEnvio': notificacion.fechaEnvio,
            'enviada': notificacion.enviada,
            'usuario_id': notificacion.usuario_id
        }

        return Response(datos)

    except Notificacion.DoesNotExist:
        return Response(
            {'error': 'Notificación no encontrada'},
            status=404
        )