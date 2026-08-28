from django.db import models

class Candidato(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'candidato'
        managed = False


class OfertaLaboral(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'ofertalaboral'
        managed = False


class EstadoPostulacion(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'estadopostulacion'
        managed = False


class Postulacion(models.Model):
    id = models.AutoField(primary_key=True)

    fechaPostulacion = models.DateField(
        null=True,
        blank=True
    )

    candidato = models.ForeignKey(
        Candidato,
        on_delete=models.CASCADE,
        db_column='candidato_id',
        null=True,
        blank=True
    )

    oferta = models.ForeignKey(
        OfertaLaboral,
        on_delete=models.CASCADE,
        db_column='oferta_id',
        null=True,
        blank=True
    )

    estado = models.ForeignKey(
        EstadoPostulacion,
        on_delete=models.CASCADE,
        db_column='estado',
        to_field='nombre',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'postulacion'
        managed = False