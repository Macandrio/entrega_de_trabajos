from django.shortcuts import render
from .models import (
    Aeropuerto, Vuelo, Pasajero, Equipaje, Aerolinea, 
    VueloAerolinea, Reserva, Empleado, Silla, Servicio, Ruta
)

def index(request):
    return render(request, 'index.html') 

# Vista para listar Aeropuertos
def lista_aeropuerto(request):
    aeropuertos = Aeropuerto.objects.all()
    return render(request, 'aeropuerto_list.html', {'aeropuertos': aeropuertos})

# Vista para listar Vuelos
def lista_vuelo(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'vuelo_list.html', {'vuelos': vuelos})

# Vista para listar Pasajeros
def lista_pasajero(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'pasajero_list.html', {'pasajeros': pasajeros})

# Vista para listar Equipajes
def lista_equipaje(request):
    equipajes = Equipaje.objects.all()
    return render(request, 'equipaje_list.html', {'equipajes': equipajes})

# Vista para listar Aerolíneas
def lista_aerolineas(request):  # Cambiado aquí
    aerolineas = Aerolinea.objects.all()
    return render(request, 'aerolinea_list.html', {'aerolineas': aerolineas})

# Vista para listar VueloAerolinea
def lista_vuelos_aerolineas(request):  # Cambiado aquí
    vuelos_aerolineas = VueloAerolinea.objects.all()
    return render(request, 'vuelo_aerolinea_list.html', {'vuelos_aerolineas': vuelos_aerolineas})

# Vista para listar Reservas
def lista_reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva_list.html', {'reservas': reservas})

# Vista para listar Empleados
def lista_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado_list.html', {'empleados': empleados})

# Vista para listar Sillas
def lista_silla(request):
    sillas = Silla.objects.all()
    return render(request, 'silla_list.html', {'sillas': sillas})

# Vista para listar Servicios
def lista_servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio_list.html', {'servicios': servicios})

# Vista para listar Rutas
def lista_ruta(request):
    rutas = Ruta.objects.all()
    return render(request, 'ruta_list.html', {'rutas': rutas})


