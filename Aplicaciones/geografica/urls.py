#URLS especificas de la aplicacion
from django.urls import path
from .views import ubicacion_vehiculo_api
from.import views
urlpatterns = [

    path('',views.inicio),
    path('inicio/', views.inicio),
    path('api/ubicacion_vehiculo/', ubicacion_vehiculo_api, name='ubicacion_vehiculo_api'),


]

