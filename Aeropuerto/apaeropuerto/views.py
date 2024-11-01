from django.shortcuts import render
from django.db.models import Prefetch, Q, Sum, Count
from .models import (
    Aeropuerto, Vuelo, Pasajero, Equipaje, Aerolinea, 
    VueloAerolinea, Reserva, Empleado, Asiento, Servicio ,ContactoAeropuerto , EstadisticasVuelo , PerfilPasajero
)

def index(request):
    return render(request, 'index.html') 

# Vista para listar Aeropuertos
def lista_aeropuerto(request):
    aeropuertos = Aeropuerto.objects.all()
    return render(request, 'paginas/aeropuerto_list.html', {'aeropuertos': aeropuertos})

# Vista para listar Vuelos
def lista_vuelo(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'paginas/vuelo_list.html', {'vuelos': vuelos})

# Vista para listar Pasajeros
def lista_pasajero(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'paginas/pasajero_list.html', {'pasajeros': pasajeros})

# Vista para listar Equipajes
def lista_equipaje(request):
    equipajes = Equipaje.objects.all()
    return render(request, 'paginas/equipaje_list.html', {'equipajes': equipajes})

# Vista para listar Aerolíneas
def lista_aerolineas(request):  # Cambiado aquí
    aerolineas = Aerolinea.objects.all()
    return render(request, 'paginas/aerolinea_list.html', {'aerolineas': aerolineas})

# Vista para listar VueloAerolinea
def lista_vuelos_aerolineas(request):  # Cambiado aquí
    vuelos_aerolineas = VueloAerolinea.objects.all()
    return render(request, 'paginas/vuelo_aerolinea_list.html', {'vuelos_aerolineas': vuelos_aerolineas})

# Vista para listar Reservas
def lista_reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'paginas/reserva_list.html', {'reservas': reservas})

# Vista para listar Empleados
def lista_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'paginas/empleado_list.html', {'empleados': empleados})

# Vista para listar Asientos
def lista_silla(request):
    sillas = Asiento.objects.all()
    return render(request, 'paginas/silla_list.html', {'sillas': sillas})

# Vista para listar Servicios
def lista_servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'paginas/servicio_list.html', {'servicios': servicios})

# Vista para listar ContactoAeropuerto
def lista_ContactoAeropuerto(request):
    contactoAero = ContactoAeropuerto.objects.all()
    return render(request, 'paginas/lista_ContactoAeropuerto_listar.html', {'contactoAero': contactoAero})

# Vista para listar EstadisticasVuelo
def lista_EstadisticasVuelo(request):
    estadisticas = EstadisticasVuelo.objects.all()
    return render(request, 'paginas/estadisticas_list.html', {'estadisticas': estadisticas})

# Vista para listar PerfilPasajero
def lista_PerfilPasajero(request):
    perfilpasajero = PerfilPasajero.objects.all()
    return render(request, 'paginas/perfilpasajero_list.html', {'perfilpasajero': perfilpasajero})


# 1. Todos los pasajeros que esten asociados a un vuelo con una relación reversa
def pasajeros_vuelo(request , id_vuelo):
    vuelo = Vuelo.objects.prefetch_related(Prefetch('vuelo_pasajero')).get(id=id_vuelo)
  
    return render(request, 'consultas/pasajeros_vuelo.html',{'vuelo': vuelo})
                         
# 2. Todos los vuelos que esten volando que esten una año en concreto

def vuelo_volando_año(request , anyo):
    datosvuelo = EstadisticasVuelo.objects.select_related('vuelo')
    datosvuelo = datosvuelo.filter(fecha_estadisticas__year = anyo, vuelo__estado = False)

    return render(request, 'consultas/vuelo_volando_año.html',{'datosvuelo': datosvuelo})

# 3. feedbacks de todos los vuelos que tenga una palabra en concreto de una aerolinea en concreto desde la tabla intermedia

def texto_vuelo_aerolinea(request, id_aerolinea, texto_buscar):
    
    aerolinea = Aerolinea.objects.get(id=id_aerolinea)

    vuelo_aerolinea = VueloAerolinea.objects.select_related('aerolinea','vuelo', 'vuelo__vuelo_datos')
    vuelo_aerolinea = vuelo_aerolinea.filter(aerolinea_id=id_aerolinea, vuelo__vuelo_datos__feedback_pasajeros__icontains=texto_buscar)
    return render(request, 'consultas/texto_vuelo_aerolinea.html', {'vuelo_aerolinea': vuelo_aerolinea, 'aerolinea': aerolinea})



# 4. Obtener el feedbacks de todos los vuelos en el que ha estado un pasajero específico.

def historial_feedbacks_pasajero(request, pasajero_id):

    pasajero = Pasajero.objects.get(id=pasajero_id) # Obtener el pasajero

    feedbacks = EstadisticasVuelo.objects.select_related('vuelo')
    feedbacks = feedbacks.filter(vuelo__vuelo_pasajero=pasajero)
    return render(request, 'consultas/historial_feedbacks_pasajero.html', {'feedbacks': feedbacks, 'pasajero': pasajero})


#5. Obtener todos los vuelos que salgan desde un aeropuerto específico y lleguen a un destino específico

def vuelos_origen_destino(request, origen_id, destino_id):
    
    vuelos = Vuelo.objects.select_related('origen', 'destino') 
    vuelos = vuelos.filter(origen_id=origen_id, destino_id=destino_id)

    return render(request, 'consultas/vuelos_origen_destino.html', {'vuelos': vuelos})


#6. Listar reservas por método de pago y año

def reservas_por_metodo_y_año(request, metodo_pago, año):
    reservas = Reserva.objects.select_related('pasajero', 'vuelo')
    reservas = reservas.filter(metodo_pago=metodo_pago,fecha_reserva__year=año)

    return render(request, 'consultas/reservas_por_metodo_y_año.html', {'reservas': reservas})


# 7. Obtener todos los vuelos que tengan un origen y destino en concreto o que el estado sea volando

def vuelos_cortos_origen_destino(request, origen_id, destino_id, estado):

    vuelos = Vuelo.objects.select_related('origen', 'destino')
    vuelos = vuelos.filter(Q(origen_id=origen_id) & Q(destino_id=destino_id) | (~Q(estado=estado)))

    return render(request, 'consultas/vuelos_cortos.html', {'vuelos': vuelos})



# 8. Calcular el peso total del equipaje de todos los pasajeros en un vuelo específico y ordenar
def peso_equipaje_vuelo(request, vuelo_id):
    
    equipajes = Equipaje.objects.select_related('pasajero')
    equipajes = equipajes.filter(pasajero__vuelo__id=vuelo_id).order_by('-peso')[:5] 
    peso_total = equipajes.aggregate(Sum('peso'))['peso__sum']  

    return render(request, 'consultas/peso_equipaje_vuelo.html', {'equipajes': equipajes,'peso_total': peso_total})

# 9. Listar todos los vuelos de una aerolínea específica que no tienen registrada una fecha de operación en la tabla intermedia
def vuelos_sin_operacion(request, aerolinea_id):

    vuelos = VueloAerolinea.objects.select_related('aerolinea', 'vuelo')
    vuelos = vuelos.filter(aerolinea_id=aerolinea_id, fecha_operacion__isnull=True)

    return render(request, 'consultas/vuelos_sin_operacion.html', {'vuelos': vuelos})



# 10. Calcular cuantos pasajeros hay en un vuelo
def cuantos_pasajeros_vuelo(request, id_vuelo):
    
    pasajeros = Pasajero.objects.prefetch_related('vuelo')
    pasajeros = pasajeros.filter(vuelo__id=id_vuelo)
    total_pasajeros = pasajeros.aggregate(Count('id'))['id__count']
    
    return render(request, 'consultas/total_pasajeros.html', {'total_pasajeros': total_pasajeros, 'pasajeros': pasajeros})


# Error 400 - Solicitud Incorrecta
def error_400(request, exception):
    return render(request, 'errors/400.html', status=400)

# Error 403 - Prohibido
def error_403(request, exception):
    return render(request, 'errors/403.html', status=403)

# Error 404 - No Encontrado
def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

# Error 500 - Error Interno del Servidor
def error_500(request):
    return render(request, 'errors/500.html', status=500)





