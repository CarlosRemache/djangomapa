from django.contrib.gis.db import models
from django.utils import timezone



class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nombre_usuario=models.CharField(max_length=100)
    apellido_usuario=models.CharField(max_length=100)
    correo_usuario=models.EmailField(unique=True)
    contrasena_usuario = models.CharField(max_length=128)




class Vehiculo(models.Model): 
    id_vehiculo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="vehiculos")
    tipovehiculo_vehiculo  = models.CharField(max_length=50, choices=[('PRIVADO', 'PRIVADO'), ('TAXI', 'TAXI'), ('MOTOCICLETA', 'MOTOCICLETA'), ('CAMION', 'CAMION')])
    tipocombustible_vehiculo  = models.CharField(max_length=50, choices=[('EXTRA', 'EXTRA'), ('DIESEL', 'DIESEL'), ('SUPER', 'SUPER')])
    matricula_vehiculo  = models.CharField(max_length=100, unique=True)
    modelo_vehiculo  = models.CharField(max_length=50, blank=True)



class UbicacionVehiculo(models.Model):
    id_ubicacion=models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="UbicacionVehiculos")
    latitud_ubicacion = models.FloatField()
    longitud_ubicacion = models.FloatField()
    fecha_hora_ubicacion = models.DateTimeField(default=timezone.now)
    punto = models.PointField(srid=4326, null=True, blank=True)   # Campo geográfico con PostGIS


    class Meta:
        ordering = ['-fecha_hora_ubicacion']

