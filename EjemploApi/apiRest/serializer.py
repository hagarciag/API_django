# This file is required for djangorestframework
# Firma, Says which fields API is going to use

from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields=[ 'num_doc','tipo_num_doc','grupo_riesgo','capacidad_pago']