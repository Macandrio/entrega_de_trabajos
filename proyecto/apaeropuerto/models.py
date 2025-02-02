from django.db import models
from django.utils  import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, RegexValidator


# Modelo Aeropuerto
class Aeropuerto(models.Model):
    PAISES = [
    ("ES", "España"),
    ("FR", "Francia"),
    ("IT", "Italia"),
    ("DE", "Alemania"),
    ("PT", "Portugal"),
    ("NL", "Países Bajos"),
    ("BE", "Bélgica"),
    ("SE", "Suecia"),
    ("AT", "Austria"),
    ("CH", "Suiza"),
    ]
    CIUDADES = [
    ("ES", "Madrid"),
    ("FR", "París"),
    ("IT", "Roma"),
    ("DE", "Berlín"),
    ("PT", "Lisboa"),
    ("NL", "Ámsterdam"),
    ("BE", "Bruselas"),
    ("SE", "Estocolmo"),
    ("AT", "Viena"),
    ("CH", "Ginebra"),
    ]


    AeropuertoS = [
    ("ES", "Aeropuerto Adolfo Suárez Madrid-Barajas"),  # Madrid, España
    ("FR", "Aeropuerto Charles de Gaulle"),             # París, Francia
    ("IT", "Aeropuerto Internacional Leonardo da Vinci"),  # Roma, Italia
    ("DE", "Aeropuerto de Berlín-Tegel"),               # Berlín, Alemania
    ("PT", "Aeropuerto de Lisboa"),                     # Lisboa, Portugal
    ("NL", "Aeropuerto de Ámsterdam-Schiphol"),        # Ámsterdam, Países Bajos
    ("BE", "Aeropuerto de Bruselas-Zaventem"),         # Bruselas, Bélgica
    ("SE", "Aeropuerto de Estocolmo-Arlanda"),         # Estocolmo, Suecia
    ("AT", "Aeropuerto Internacional de Viena"),       # Viena, Austria
    ("CH", "Aeropuerto de Ginebra"),                   # Ginebra, Suiza
]



    nombre = models.CharField(
        max_length=2,
        choices=AeropuertoS, default='ES',
        verbose_name="Aeropuerto"
    )
    ciudades = models.CharField(
        max_length=2,
        choices=CIUDADES,default='ES'
    ) 
    pais = models.CharField(
        max_length=2,
        choices=PAISES, default='ES'
    ) 
    capacidad_maxima = models.IntegerField(default=150) # Campo por defecto

    def __str__(self):
        return self.nombre
    


# Modelo Vuelo
class Vuelo(models.Model):
    numero_vuelo_dia = models.IntegerField(db_column='veces_volado_dia',blank=False,error_messages={'blank': 'Este campo no puede estar vacío.',})
    hora_salida = models.DateTimeField()
    hora_llegada = models.DateTimeField()
    volando  = models.BooleanField() #boolean
    duracion = models.DurationField(editable=False)  # Duración del vuelo
    aeropuerto = models.ForeignKey(Aeropuerto , on_delete=models.CASCADE)  # Relación ManyToOne


    def save(self, *args, **kwargs):
        # Calcular la duración como la diferencia entre hora_llegada y hora_salida
        if self.hora_llegada and self.hora_salida:
            self.duracion = self.hora_llegada - self.hora_salida
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.numero_vuelo_dia}"


# Modelo Pasajero

def validar_dominio_email(email):
    # Lista de dominios permitidos
        dominios_permitidos = ['@gmail.com', '@hotmail.com', '@polignosur.org']
    
    # Comprobar si el correo electrónico termina con alguno de los dominios permitidos
        if not any(email.endswith(dominio) for dominio in dominios_permitidos):
            raise ValidationError(
                _('El correo electrónico debe tener uno de los siguientes dominios: @gmail.com, @hotmail.com, @polignosur.org.'),
                code='invalid_domain',
            )
        
class Pasajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, blank=True)  # Permitir valores vacíos
    email = models.EmailField(validators=[validar_dominio_email])
    telefono = models.CharField(
        max_length=9,
        validators=[
            MaxLengthValidator(9),
            RegexValidator(regex=r'^\d{9}$', message='El número de teléfono debe tener exactamente 9 dígitos.')
        ],
        blank=True  # Permitir que este campo esté vacío si es necesario
    )
    fecha_nacimiento = models.DateField(null=True)  
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE) # Relación ManyToOne


    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        

    
# Modelo Equipaje
class Equipaje(models.Model):
    peso = models.FloatField()
    dimensiones = models.CharField(max_length=50)
    tipo_material = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE)  # Relación OneToOne
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE) # Relación ManyToOne

    def __str__(self):
        return f"Equipaje de {self.pasajero.nombre} {self.pasajero.apellido}"


# Modelo Aerolínea
class Aerolinea(models.Model):

    paises = [
        ("ES", "España"),
        ("EN", "Inglaterra"),
        ("FR", "Francia"),
        ("IT", "Italia"),
    ]

    nombre = models.CharField(max_length=100,verbose_name="Aerolínea operadora")
    codigo = models.CharField(max_length=10)
    fecha_fundacion = models.DateField(auto_now_add=True)
    pais = models.CharField(
        max_length=2,
        choices=paises,default='ES'
    )
    aeropuerto =   models.ManyToManyField(Aeropuerto) # Relación ManytoMany

    def __str__(self):
        return self.nombre



# Tabla intermedia Vuelo_Aerolinea
class VueloAerolinea(models.Model):
    tipos_clase_avion = [
    ("E", "Economy"),
    ("B", "Business"),
    ("F", "First Class"),
    ("P", "Premium Economy"),
    ("L", "Luxury"),
    ("S", "Standard"),
    ("H", "Hybrid"),
    ("X", "Extra Legroom"),
    ("R", "Regional"),
    ("C", "Charter")
    ]

    fecha_operacion = models.DateTimeField(null=True)
    estado = models.TextField()
    clase = models.CharField(max_length=1,choices=tipos_clase_avion, default='E')
    numero_de_vuelos = models.IntegerField(default=5)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación OneToMany
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE) # Relación OneToMany
  


# Modelo Reserva
class Reserva(models.Model):

    METODO_PAGO_CHOICES = [
        ('tarjeta', 'Tarjeta de crédito'),
        ('efectivo', 'Efectivo'),
        ('paypal', 'PayPal'),
    ]
    fecha_reserva = models.DateTimeField(default=timezone.now)  # Valor por defecto: fecha y hora actuales
    estado = models.CharField(max_length=50,help_text="Introduce Como va el avion durante el vuelo")
    metodo_pago = models.CharField(max_length=10, 
                                   choices=METODO_PAGO_CHOICES,
                                   default= 'tarjeta')
    estado_de_pago = models.BooleanField(default=False)
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE)  # Relación OneToOne
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToOne

    def __str__(self):
        return f"Reserva de {self.pasajero.nombre} {self.pasajero.apellido}"


# Modelo Empleado
class Empleado(models.Model):
    CARGO = [
        ('JE', 'Jefe'),
        ('EM', 'Empleado'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=2,choices=CARGO,default='EM')
    fecha_contratacion = models.DateField()
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)   # Relación ManyToOne
    vuelos = models.ManyToManyField(Vuelo) #Relacion ManyToMany


    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.cargo} en {self.aeropuerto.nombre}"


# Modelo Silla (para Vuelo)
class Silla(models.Model):
    tipos_clase_avion = [
    ("E", "Economy"),
    ("B", "Business"),
    ("F", "First Class"),
    ("P", "Premium Economy"),
    ("L", "Luxury"),
    ("S", "Standard"),
    ("H", "Hybrid"),
    ("X", "Extra Legroom"),
    ("R", "Regional"),
    ("C", "Charter")
    ]

    numero = models.IntegerField()
    clase = models.CharField(max_length=1,choices=tipos_clase_avion,default='E')
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    posicion = models.IntegerField()
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToOne
    pasajero = models.OneToOneField(Pasajero,on_delete=models.CASCADE)  # Relación OneToOne 

    def __str__(self):
        return f"Silla {self.numero} ({self.clase})"


# Modelo Servicio
class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=100)
    costo = models.FloatField()
    duracion_servicio = models.TimeField()
    añadido = models.CharField(max_length=100)

    aeropuerto = models.OneToOneField(Aeropuerto, on_delete=models.CASCADE)  # Relación OneToOne
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToOne
    pasajeros = models.ManyToManyField(Pasajero)  # Relación ManyToMany

    def __str__(self):
        return self.tipo_servicio


# Modelo Ruta
class Ruta(models.Model):
    salida = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    duracion = models.TimeField()
    distancia = models.FloatField()
    aeropuerto = models.ManyToManyField(Aeropuerto) # Relacion ManyToMany


    def __str__(self):
        return self.destino
