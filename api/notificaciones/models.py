from django.db import models


class Notificacion(models.Model):
	destinatario = models.CharField(max_length=255, db_column='destinario')
	mensaje = models.TextField()
	fechaEnvio = models.DateTimeField(auto_now_add=True)
	enviada = models.BooleanField(default=False)
	usuario_id = models.IntegerField()

	class Meta:
		db_table = 'notificacion'
		managed = False
		ordering = ['-fechaEnvio']

	def __str__(self):
		return f'Notificacion para {self.destinatario}'
