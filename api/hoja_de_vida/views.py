from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import HojaDeVida


@api_view(['GET'])
def listar_hojas_de_vida(request):
    hojas = HojaDeVida.objects.all()

    datos = []

    for hoja in hojas:
        datos.append({
            'id': hoja.id,
            'urlArchivo': hoja.urlArchivo,
            'fechaCarga': hoja.fechaCarga,
            'tamanoMB': hoja.tamanoMB,
            'candidato_id': hoja.candidato_id
        })

    return Response(datos)


@api_view(['GET'])
def obtener_hoja_de_vida(request, id):
    try:
        hoja = HojaDeVida.objects.get(id=id)

        datos = {
            'id': hoja.id,
            'urlArchivo': hoja.urlArchivo,
            'fechaCarga': hoja.fechaCarga,
            'tamanoMB': hoja.tamanoMB,
            'candidato_id': hoja.candidato_id
        }

        return Response(datos)

    except HojaDeVida.DoesNotExist:
        return Response(
            {'error': 'Hoja de vida no encontrada'},
            status=404
        )