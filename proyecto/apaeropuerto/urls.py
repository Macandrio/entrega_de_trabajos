from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aeropuerto/', views.lista_aeropuerto, name='lista_aeropuerto'),
    path('vuelo/', views.lista_vuelo, name='lista_vuelo'),
    path('pasajero/', views.lista_pasajero, name='lista_pasajero'),
    path('equipaje/', views.lista_equipaje, name='lista_equipaje'),
    path('aerolinea/', views.lista_aerolinea, name='lista_aerolinea'),
    path('vuelo_aerolinea/', views.lista_vuelo_aerolinea, name='lista_vuelo_aerolinea'),
    path('reserva/', views.lista_reserva, name='lista_reserva'),
    path('empleado/', views.lista_empleado, name='lista_empleado'),
    path('silla/', views.lista_silla, name='lista_silla'),
    path('servicio/', views.lista_servicio, name='lista_servicio'),
    path('ruta/', views.lista_ruta, name='lista_ruta'),
]