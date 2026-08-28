from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Postulacion


@api_view(['GET'])
def listar_postulaciones(request):
    postulaciones = Postulacion.objects.all()

    datos = []

    for postulacion in postulaciones:
        datos.append({
            'id': postulacion.id,
            'fechaPostulacion': postulacion.fechaPostulacion,
            'candidato_id': postulacion.candidato_id,
            'oferta_id': postulacion.oferta_id,
            'estado': postulacion.estado_id
        })

    return Response(datos)


@api_view(['GET'])
def obtener_postulacion(request, id):
    try:
        postulacion = Postulacion.objects.get(id=id)

        datos = {
            'id': postulacion.id,
            'fechaPostulacion': postulacion.fechaPostulacion,
            'candidato_id': postulacion.candidato_id,
            'oferta_id': postulacion.oferta_id,
            'estado': postulacion.estado_id
        }

        return Response(datos)

    except Postulacion.DoesNotExist:
        return Response(
            {'error': 'Postulación no encontrada'},
            status=404
        )