api/ofertas/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import OfertaLaboral


@api_view(['GET'])
def listar_ofertas(request):
    ofertas = OfertaLaboral.objects.all()

    datos = []

    for oferta in ofertas:
        datos.append({
            'id': oferta.id,
            'titulo': oferta.titulo,
            'descripcion': oferta.descripcion,
            'salario': oferta.salario,
            'ciudad': oferta.ciudad,
            'area': oferta.area_id,
            'modalidad': oferta.modalidad_id,
            'aprobada': oferta.aprobada,
            'fechaPublicacion': oferta.fechaPublicacion,
            'empleador_id': oferta.empleador_id
        })

    return Response(datos)


@api_view(['GET'])
def obtener_oferta(request, id):
    try:
        oferta = OfertaLaboral.objects.get(id=id)

        datos = {
            'id': oferta.id,
            'titulo': oferta.titulo,
            'descripcion': oferta.descripcion,
            'salario': oferta.salario,
            'ciudad': oferta.ciudad,
            'area': oferta.area_id,
            'modalidad': oferta.modalidad_id,
            'aprobada': oferta.aprobada,
            'fechaPublicacion': oferta.fechaPublicacion,
            'empleador_id': oferta.empleador_id
        }

        return Response(datos)

    except OfertaLaboral.DoesNotExist:
        return Response(
            {'error': 'Oferta laboral no encontrada'},
            status=404
        )