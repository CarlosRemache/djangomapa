from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UbicacionVehiculo
from .serializers import UbicacionVehiculoSerializer


# Create your views here.
def inicio(request):
    return render(request,'inicio.html')





@api_view(['GET', 'POST'])
def ubicacion_vehiculo_api(request):
    # Cuando el teléfono envía coordenadas (POST)
    if request.method == 'POST':
        serializer = UbicacionVehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Cuando el mapa consulta la última ubicación (GET)
    elif request.method == 'GET':
        ultima = UbicacionVehiculo.objects.last()
        if ultima:
            serializer = UbicacionVehiculoSerializer(ultima)
            return Response(serializer.data)
        return Response({'latitud': None, 'longitud': None})
