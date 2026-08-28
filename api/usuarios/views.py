from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Usuario


@api_view(['GET'])
def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    datos = []

    for usuario in usuarios:
        datos.append({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'rol': usuario.rol_id,
            'activo': usuario.activo,
            'fechaRegistro': usuario.fechaRegistro
        })

    return Response(datos)