from django.db import models

# Modelo Aeropuerto
class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_iata = models.CharField(max_length=3)  

    def __str__(self):
        return self.nombre


# Modelo Vuelo
class Vuelo(models.Model):
    numero_vuelo = models.CharField(max_length=10)
    hora_salida = models.DateTimeField()
    hora_llegada = models.DateTimeField()
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)  # Relación ManyToOne
    estado = models.CharField(max_length=20)  

    def __str__(self):
        return self.numero_vuelo


# Modelo Pasajero
class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo Equipaje (OneToOne con Pasajero)
class Equipaje(models.Model):
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE)  # Relación OneToOne
    peso = models.FloatField()
    dimensiones = models.CharField(max_length=50)
    tipo_material = models.CharField(max_length=30)  

    def __str__(self):
        return f"Equipaje de {self.pasajero.nombre} {self.pasajero.apellido}"


# Modelo Aerolínea
class Aerolinea(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()  

    def __str__(self):
        return self.nombre


# Tabla intermedia Vuelo_Aerolinea
class VueloAerolinea(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToMany con atributos extras
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE)
    fecha_operacion = models.DateTimeField()
    estado = models.CharField(max_length=50)
    precio = models.FloatField()  

    def __str__(self):
        return f"Vuelo {self.vuelo.numero_vuelo} operado por {self.aerolinea.nombre}"


# Modelo Reserva
class Reserva(models.Model):
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)  # Relación ManyToOne
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToOne
    fecha_reserva = models.DateTimeField()
    estado = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)  

    def __str__(self):
        return f"Reserva de {self.pasajero.nombre} {self.pasajero.apellido} para vuelo {self.vuelo.numero_vuelo}"


# Modelo Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    aeropuerto = models.OneToOneField(Aeropuerto, on_delete=models.CASCADE)  # Relación OneToOne
    fecha_contratacion = models.DateField()  

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.cargo} en {self.aeropuerto.nombre}"


# Modelo Silla (para Vuelo)
class Silla(models.Model):
    numero = models.IntegerField()
    clase = models.CharField(max_length=20)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToOne
    precio = models.FloatField()  

    def __str__(self):
        return f"Silla {self.numero} ({self.clase}) en vuelo {self.vuelo.numero_vuelo}"


# Modelo Servicio
class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=100)
    costo = models.FloatField()
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)  # Relación ManyToOne
    duracion = models.IntegerField()  

    def __str__(self):
        return self.tipo_servicio


# Modelo Ruta
class Ruta(models.Model):
    origen = models.ForeignKey(Aeropuerto, related_name='rutas_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Aeropuerto, related_name='rutas_destino', on_delete=models.CASCADE)
    duracion = models.IntegerField()
    distancia = models.FloatField()  

    def __str__(self):
        return f"Ruta de {self.origen.nombre} a {self.destino.nombre}"
