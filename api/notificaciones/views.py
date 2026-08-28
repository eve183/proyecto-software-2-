import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Notificacion


@require_POST
def crear_notificacion(request):
	try:
		datos = json.loads(request.body)
		notificacion = Notificacion.objects.create(
			destinatario=datos['destinatario'],
			mensaje=datos['mensaje'],
			enviada=datos.get('enviada', False),
			usuario_id=datos['usuario_id'],
		)
	except (json.JSONDecodeError, KeyError, TypeError, ValueError):
		return JsonResponse(
			{
				'error': (
					'Envía destinatario, mensaje y usuario_id en formato JSON.'
				)
			},
			status=400,
		)

	return JsonResponse(
		{
			'id': notificacion.id,
			'destinatario': notificacion.destinatario,
			'mensaje': notificacion.mensaje,
			'fechaEnvio': notificacion.fechaEnvio,
			'enviada': notificacion.enviada,
			'usuario_id': notificacion.usuario_id,
		},
		status=201,
	)
