from django.shortcuts import render
from .models import (
    Aeropuerto, Vuelo, Pasajero, Equipaje, Aerolinea, 
    VueloAerolinea, Reserva, Empleado, Silla, Servicio, Ruta
)

def index(request):
    return render(request, 'index.html') 


# Vista para listar Aeropuertos
def lista_aeropuerto(request):
    aeropuertos = Aeropuerto.objects.all()  # Obtener todos los aeropuertos
    return render(request, 'aeropuerto_list.html', {'aeropuertos': aeropuertos})

# Vista para listar Vuelos
def lista_vuelo(request):
    vuelos = Vuelo.objects.all()  # Obtener todos los vuelos
    return render(request, 'vuelo_list.html', {'vuelos': vuelos})

# Vista para listar Pasajeros
def lista_pasajero(request):
    pasajeros = Pasajero.objects.all()  # Obtener todos los pasajeros
    return render(request, 'pasajero_list.html', {'pasajeros': pasajeros})

# Vista para listar Equipajes
def lista_equipaje(request):
    equipajes = Equipaje.objects.all()  # Obtener todos los equipajes
    return render(request, 'equipaje_list.html', {'equipajes': equipajes})

# Vista para listar Aerolíneas
def lista_aerolinea(request):
    aerolineas = Aerolinea.objects.all()  # Obtener todas las aerolíneas
    return render(request, 'aerolinea_list.html', {'aerolineas': aerolineas})

# Vista para listar VueloAerolinea (relación intermedia entre vuelo y aerolínea)
def lista_vuelo_aerolinea(request):
    vuelos_aerolineas = VueloAerolinea.objects.all()  # Obtener todos los registros de vuelos-aerolíneas
    return render(request, 'vuelo_aerolinea_list.html', {'vuelos_aerolineas': vuelos_aerolineas})

# Vista para listar Reservas
def lista_reserva(request):
    reservas = Reserva.objects.all()  # Obtener todas las reservas
    return render(request, 'reserva_list.html', {'reservas': reservas})

# Vista para listar Empleados
def lista_empleado(request):
    empleados = Empleado.objects.all()  # Obtener todos los empleados
    return render(request, 'empleado_list.html', {'empleados': empleados})

# Vista para listar Sillas
def lista_silla(request):
    sillas = Silla.objects.all()  # Obtener todas las sillas
    return render(request, 'silla_list.html', {'sillas': sillas})

# Vista para listar Servicios
def lista_servicio(request):
    servicios = Servicio.objects.all()  # Obtener todos los servicios
    return render(request, 'servicio_list.html', {'servicios': servicios})

# Vista para listar Rutas
def lista_ruta(request):
    rutas = Ruta.objects.all()  # Obtener todas las rutas
    return render(request, 'ruta_list.html', {'rutas': rutas})