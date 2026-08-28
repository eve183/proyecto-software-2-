from django.contrib import admin
from .models import Notificacion


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
	list_display = ('id', 'destinatario', 'fechaEnvio', 'enviada', 'usuario_id')
	list_filter = ('enviada', 'fechaEnvio')
