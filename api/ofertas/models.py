from django.db import models


class Empleador(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'empleador'
        managed = False


class AreaProfesional(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

    class Meta:
        db_table = 'areaprofesional'
        managed = False


class ModalidadTrabajo(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'modalidadtrabajo'
        managed = False


class OfertaLaboral(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    salario = models.FloatField(null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    aprobada = models.BooleanField(null=True, blank=True)
    fechaPublicacion = models.DateField(null=True, blank=True)

    empleador = models.ForeignKey(
        Empleador,
        on_delete=models.CASCADE,
        db_column='empleador_id',
        null=True,
        blank=True
    )

    area = models.ForeignKey(
        AreaProfesional,
        on_delete=models.CASCADE,
        db_column='area',
        to_field='nombre',
        null=True,
        blank=True
    )

    modalidad = models.ForeignKey(
        ModalidadTrabajo,
        on_delete=models.CASCADE,
        db_column='modalidad',
        to_field='nombre',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'ofertalaboral'
        managed = False