from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aeropuerto/', views.lista_aeropuerto, name='lista_aeropuerto'),
    path('vuelo/', views.lista_vuelo, name='lista_vuelo'),
    path('pasajero/', views.lista_pasajero, name='lista_pasajero'),
    path('equipaje/', views.lista_equipaje, name='lista_equipaje'),
    path('aerolineas/', views.lista_aerolineas, name='lista_aerolineas'),
    path('vuelos_aerolineas/', views.lista_vuelos_aerolineas, name='lista_vuelos_aerolineas'),
    path('reserva/', views.lista_reserva, name='lista_reserva'),
    path('empleado/', views.lista_empleado, name='lista_empleado'),
    path('silla/', views.lista_silla, name='lista_silla'),
    path('servicio/', views.lista_servicio, name='lista_servicio'),
    path('contactoaeropuerto/', views.lista_ContactoAeropuerto, name='lista_ContactoAeropuerto'),
    path('estadisticasvuelo/', views.lista_EstadisticasVuelo, name='lista_EstadisticasVuelo'),
    path('datospasajero/', views.lista_PerfilPasajero, name='lista_PerfilPasajero'),

    #QuerySet
    path('pasajero-vuelo/<int:id_vuelo>/', views.pasajeros_vuelo, name='pasajeros_vuelo'),
    path('vuelo-volando-año/<int:anyo>/', views.vuelo_volando_año, name='vuelo_volando_año'),
    path('texto-vuelo-aerolinea/<int:id_aerolinea>/<str:texto_buscar>/', views.texto_vuelo_aerolinea, name='texto_vuelo_aerolinea'),
    path('historial-feedbacks-pasajero/<int:pasajero_id>/', views.historial_feedbacks_pasajero, name='historial_feedbacks_pasajero'),
    path('vuelos-origen-destino/<int:origen_id>/<int:destino_id>/', views.vuelos_origen_destino, name='vuelos_origen_destino'),
    re_path(r'^reservas/(?P<metodo_pago>\w+)/(?P<año>\d{4})/$', views.reservas_por_metodo_y_año, name='reservas_por_metodo_y_año'),
    path('vuelos/cortos/<int:origen_id>/<int:destino_id>/<int:estado>/', views.vuelos_cortos_origen_destino, name='vuelos_cortos_origen_destino'),
    path('peso-equipaje-vuelo/<int:vuelo_id>/', views.peso_equipaje_vuelo, name='peso_equipaje_vuelo'),
    path('vuelos-sin-operacion/<int:aerolinea_id>/', views.vuelos_sin_operacion, name='vuelos_sin_operacion'),
    path('consulta/pasajeros-vuelo/<int:id_vuelo>/', views.cuantos_pasajeros_vuelo, name='cuantos_pasajeros_vuelo'),





]
