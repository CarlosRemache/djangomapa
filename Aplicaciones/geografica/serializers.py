from rest_framework import serializers
from .models import UbicacionVehiculo

class UbicacionVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UbicacionVehiculo
        fields = ['id', 'latitud', 'longitud', 'fecha_hora']
