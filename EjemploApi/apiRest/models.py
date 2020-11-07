from django.db import models

# Create your models here.
# Every class represent a table and every variable an column of the table
class Cliente(models.Model):
    num_doc = models.TextField(max_length=15)
    tipo_num_doc=models.TextField(max_length=1)
    grupo_riesgo=models.TextField(max_length=3)
    capacidad_pago = models.FloatField()