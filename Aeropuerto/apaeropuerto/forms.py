from django import forms
from django.forms import ModelForm
from .models import *
from datetime import *
import re 
from django.utils import timezone
from .forms import *





#------------------------------------------------------------Aeropuerto---------------------------------------------------------------------------------------

class AeropuertoForm(ModelForm):
    class Meta:
        model = Aeropuerto  # Asociamos el formulario con el modelo Aeropuerto
        fields='__all__'

        #Como se muestra en el formulario
        labels= {
            "nombre" : ("Nombre del Aeropuerto"),
            "ciudades" : ("Ciudad del aeropuerto"),
            "pais" : ("Pais del aeropuerto"),
            "capacidad_maxima" : ("Capacidad del aeropuerto"),
        }

        widgets = {

            "nombre": forms.TextInput(attrs={
                "placeholder": "Introduce el nombre del aeropuerto",  # Ayuda al usuario
                "maxlength": 100  # Limita la cantidad de caracteres
            }),

            "ciudades": forms.Select(),
            "pais": forms.Select(),

            "capacidad_maxima": forms.NumberInput(attrs={
                "placeholder": "Introduce la capacidad máxima",  # Texto de ayuda
                "min": 0,  # Valor mínimo permitido
                "max": 150  # Valor máximo permitido
            })
            
        }

    def clean(self):
            super().clean()
            
            nombre = self.cleaned_data.get('nombre') 
            capacidad_maxima = self.cleaned_data.get('capacidad_maxima') 
            
            #Comprobamos que no exista un libro con ese nombre
            encontrar_aeropuerto = Aeropuerto.objects.filter(nombre=nombre).first()

            if(encontrar_aeropuerto):
                self.add_error('nombre','Ya existe un Aeropuerto con ese nombre')

            if(nombre == " "):
                self.add_error("nombre","El nombre del aeropuerto no puede estar vacio")
                
            if(capacidad_maxima > 150):
                self.add_error("capacidad_maxima","No puede haber mas de 150 mil personas")
            
            return self.cleaned_data

class BusquedaAvanzadaAeropuertoForm(forms.Form):
    
    textoBusqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    ciudades = forms.ChoiceField(
        choices=Aeropuerto.CIUDADES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    pais = forms.ChoiceField(
        choices=Aeropuerto.PAISES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    
    
    def clean(self):
 
        #Validamos con el modelo actual
        super().clean()
        
        #Obtenemos los campos 
        textoBusqueda = self.cleaned_data.get('textoBusqueda')
        
           
        #Controlamos los campos
        #Ningún campo es obligatorio, pero al menos debe introducir un valor en alguno para buscar
        if(textoBusqueda == ""):
            self.add_error('textoBusqueda','Debe introducir al menos un valor en un campo del formulario')
        else:
            #Si introduce un texto al menos que tenga  1 caracteres o más
            if(textoBusqueda != "" and len(textoBusqueda) < 2):
                self.add_error('textoBusqueda','Debe introducir al menos 1 caracteres')
            
        #Siempre devolvemos el conjunto de datos.
        return self.cleaned_data
    
#------------------------------------------------------------ContactoAeropuerto---------------------------------------------------------------------------------------

class ContactoAeropuertoform(ModelForm):
    class Meta:
        model=ContactoAeropuerto
        fields='__all__'
        labels = {
            "nombre_contacto": "Nombre del contacto",
            "telefono_contacto": "Teléfono de contacto",
            "email_contacto": "Correo electrónico",
            "años_trabajados": "Años trabajados en el aeropuerto",
            "aeropuerto": "Aeropuerto asociado",
        }


        widgets = {
            "nombre_contacto": forms.TextInput(attrs={
                "placeholder": "Introduce el nombre del contacto",
            }),
            "telefono_contacto": forms.TextInput(attrs={
                "placeholder": "Introduce el teléfono",
                "maxlength": 9,
            }),
            "email_contacto": forms.EmailInput(attrs={
                "placeholder": "Introduce el correo electrónico",
            }),
            "años_trabajados": forms.NumberInput(attrs={
                "placeholder": "Años trabajados",
                "min": 0,
            }),
            "aeropuerto": forms.Select(),
        }



    
    def clean(self):
        
        super().clean()
        
        telefono = self.cleaned_data.get('telefono_contacto')
        nombre_contacto = self.cleaned_data.get('nombre_contacto')

        if (nombre_contacto == ''):
            raise forms.ValidationError("nombre_contacto","El Nombre no puede estar vacio.")
        
        if len(telefono) > 999999999:
            raise forms.ValidationError("telefono","El teléfono no puede tener más de 9 dígitos.")

        return self.cleaned_data    

class BusquedaAvanzadaContacto(forms.Form):
    
    nombre_contacto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    telefono_contacto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    años_trabajados = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )


    def clean(self):
        super().clean()

        nombre_contacto = self.cleaned_data.get('nombre_contacto')
        telefono_contacto = self.cleaned_data.get('telefono_contacto')
        años_trabajados = self.cleaned_data.get('años_trabajados')

        # Validación: Al menos un campo debe estar rellenado
        if not nombre_contacto and not telefono_contacto and not años_trabajados:
            self.add_error('nombre_contacto', 'Se debe rellenar minimo un campo')
            self.add_error('telefono_contacto', 'Se debe rellenar minimo un campo')
            self.add_error('años_trabajados', 'Se debe rellenar minimo un campo')

        # Validación de puntuación
        if años_trabajados is not None and años_trabajados < 0:
            self.add_error('años_trabajados', 'Los años trabajado no puede ser menor a 0.')

        return self.cleaned_data
    
#------------------------------------------------------------Estadisticas vuelo---------------------------------------------------------------------------------------

class estadisticasvueloform(ModelForm):
    class Meta:
        model=EstadisticasVuelo
        fields='__all__'
        labels= {
            "fecha_estadisticas" : ("Fecha de la estadistica"),
            "numero_asientos_vendidos" : ("Resultado de la los asientos vendidos"),
            "numero_cancelaciones" : ("Resultado de la los asientos cancelados"),
            "feedback_pasajeros" : ("Comentario del cliente"),
        }
        widgets = {
            "fecha_estadisticas" : forms.SelectDateWidget(),
            "numero_asientos_vendidos" : forms.NumberInput(),
            "numero_cancelaciones" : forms.NumberInput(),
            "feedback_pasajeros":forms.TextInput(),
        }
    
    def clean(self):
        
        super().clean()
        
        numero_asientos_vendidos =self.cleaned_data.get('numero_asientos_vendidos') 
        numero_cancelaciones = self.cleaned_data.get('numero_cancelaciones') 
        
        
        if(numero_cancelaciones > numero_asientos_vendidos):
            self.add_error("numero_cancelaciones","No puede ver mas asientos cancelados que vendidos")
            
        if(numero_asientos_vendidos < 0):
            self.add_error("numero_asientos_vendidos","Tiene que ser mayor a 0")
            
        return self.cleaned_data

class BusquedaAvanzadaEstadisticas(forms.Form):
    
    fecha_estadisticas = forms.DateField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Fecha y Hora',
            'type' : 'date'
        })
    )

    numero_asientos_vendidos = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    numero_cancelaciones = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    def clean(self):
        super().clean()

        fecha_estadisticas = self.cleaned_data.get('fecha_estadisticas')
        numero_asientos_vendidos = self.cleaned_data.get('numero_asientos_vendidos')
        numero_cancelaciones = self.cleaned_data.get('numero_cancelaciones')

        # Validación: Al menos un campo debe estar rellenado
        if not fecha_estadisticas and not numero_asientos_vendidos and not numero_cancelaciones:
            self.add_error('fecha_estadisticas', 'Se debe rellenar minimo un campo')
            self.add_error('numero_asientos_vendidos', 'Se debe rellenar minimo un campo')
            self.add_error('numero_cancelaciones', 'Se debe rellenar minimo un campo')

        
        # Validar que ambos campos tengan valores válidos antes de compararlos
        if numero_asientos_vendidos is not None and numero_cancelaciones is not None:
            if numero_asientos_vendidos < numero_cancelaciones:
                self.add_error('numero_cancelaciones', 'Los asientos vendidos no pueden ser mayores a los cancelados.')

        return self.cleaned_data
#------------------------------------------------------------Aerolínea----------------------------------------------------------------------------------------------

class Aerolineaform(ModelForm):
    class Meta:
        model=Aerolinea
        fields='__all__'
        labels = {
            "nombre": "Nombre de la aerolínea",
            "codigo_aerolinea": "Código de la aerolínea",
            "pais_origen": "País de origen",
            "numero_aviones": "Número de aviones",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Introduce el nombre de la aerolínea",
                "maxlength": 100,
            }),
            "codigo_aerolinea": forms.TextInput(attrs={
                "placeholder": "Introduce el código de la aerolínea",
                "maxlength": 10,
            }),
            "pais_origen": forms.Select(),

            "numero_aviones": forms.NumberInput(attrs={
                "placeholder": "Introduce el número de aviones",
                "min": 0,
            }),
        }

    
    def clean(self):
        
        super().clean()
        
        nombre =self.cleaned_data.get('nombre') 
        codigo_aerolinea = self.cleaned_data.get('codigo_aerolinea') 

        #Comprobamos que no exista un libro con ese nombre
        encontrar_aerolinea = Aeropuerto.objects.filter(nombre=nombre).first()

        if(encontrar_aerolinea):
            self.add_error('nombre','Ya existe una Aerolinea con ese nombre')
        
        if(nombre == ""):
            self.add_error("nombre","No puede dejar el campo vacio")
            
        if(codigo_aerolinea == ""):
            self.add_error("codigo_aerolinea","No puede dejar el campo vacio")
            
        return self.cleaned_data

class BusquedaAvanzadaAerolinea(forms.Form):
    
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    codigo = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    pais = forms.ChoiceField(
        choices=Aerolinea.paises,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )





    def clean(self):
        super().clean()

        nombre = self.cleaned_data.get('nombre')
        codigo = self.cleaned_data.get('codigo')
        pais = self.cleaned_data.get('pais')

        #Validación: Al menos un campo debe estar rellenado
        if not nombre and not codigo and not pais:
            self.add_error('nombre', 'Se debe rellenar minimo un campo')
            self.add_error('codigo', 'Se debe rellenar minimo un campo')
            self.add_error('pais', 'Se debe rellenar minimo un campo')

        
        # Validación de puntuación
        if nombre is not None and len(nombre) < 3:
            self.add_error('nombre', 'El nombre debe de tener minimo 3 caracteres.')

        return self.cleaned_data
    
#------------------------------------------------------------Vuelo---------------------------------------------------------------------------------------------------

class VueloForm(ModelForm):
    class Meta:
        model = Vuelo
        fields = '__all__'  # Incluir todos los campos del modelo

        labels = {
            "codigo_vuelo": "Código del vuelo",
            "origen": "Aeropuerto de origen",
            "destino": "Aeropuerto de destino",
            "hora_salida": "Hora de salida",
            "hora_llegada": "Hora de llegada",
            "estado": "Estado del vuelo",
            "capacidad_maxima": "Capacidad máxima",
        }

        widgets = {
            "codigo_vuelo": forms.TextInput(attrs={
                "placeholder": "Introduce el código del vuelo",
                "maxlength": 10,
            }),

            "origen": forms.Select(),
            "destino": forms.Select(),

            "hora_salida": forms.DateTimeInput(attrs={
                "type": "datetime-local",  # Input para fecha y hora
            }),

            "hora_llegada": forms.DateTimeInput(attrs={
                "type": "datetime-local",  # Input para fecha y hora
            }),

            "estado": forms.CheckboxInput(),
            "capacidad_maxima": forms.NumberInput(attrs={
                "placeholder": "Introduce la capacidad máxima",
                "min": 1,
            }),
        }


    def clean(self):
        cleaned_data = super().clean()

        origen = cleaned_data.get('origen')
        destino = cleaned_data.get('destino')
        hora_salida = cleaned_data.get('hora_salida')
        hora_llegada = cleaned_data.get('hora_llegada')

        # Validar que el origen y destino no sean iguales
        if origen == destino:
            self.add_error('destino', "El aeropuerto de destino no puede ser el mismo que el de origen.")
            self.add_error('origen', "El aeropuerto de origen no puede ser el mismo que el de destino.")

        # Validar que la hora de llegada sea posterior a la hora de salida
        if hora_salida and hora_llegada and hora_llegada <= hora_salida:
            self.add_error('hora_llegada', "La hora de llegada debe ser posterior a la hora de salida.")

        return cleaned_data

class BusquedaAvanzadaVuelo(forms.Form):
    hora_salida = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Selecciona fecha y hora...',
            'type': 'datetime-local'  # Campo para fecha y hora
        })
    )

    hora_llegada = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Selecciona fecha y hora...',
            'type': 'datetime-local'  # Campo para fecha y hora
        })
    )

    origen = forms.ModelChoiceField(
        queryset=Aeropuerto.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    destino = forms.ModelChoiceField(
        queryset=Aeropuerto.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    aerolinea = forms.ModelChoiceField(
        queryset=Aerolinea.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    def clean(self):
        super().clean()

        hora_salida = self.cleaned_data.get('hora_salida')
        hora_llegada = self.cleaned_data.get('hora_llegada')
        origen = self.cleaned_data.get('origen')
        destino = self.cleaned_data.get('destino')

        # Validar que ambas fechas existan antes de compararlas
        if hora_salida and hora_llegada:
            if hora_salida > hora_llegada:
                self.add_error('hora_llegada', 'La hora de llegada no puede ser menor a la hora de salida.')

        # Validar que origen y destino no sean iguales
        if origen and destino:
            if origen == destino:
                self.add_error('destino', 'El destino no puede ser igual al origen.')

        return self.cleaned_data

    
#------------------------------------------------------------Pasajero-----------------------------------------------------------------------------------------------

class PasajeroForm(ModelForm):
    class Meta:
        model = Pasajero
        fields = '__all__'  # Incluir todos los campos del modelo

        labels = {
            "nombre": "Nombre del pasajero",
            "apellido": "Apellido del pasajero",
            "email": "Correo electrónico",
            "telefono": "Teléfono",
            "fecha_nacimiento": "Fecha de nacimiento",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Introduce el nombre del pasajero",
                "maxlength": 50,
            }),
            "apellido": forms.TextInput(attrs={
                "placeholder": "Introduce el apellido del pasajero",
                "maxlength": 50,
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Introduce el correo electrónico",
            }),
            "telefono": forms.TextInput(attrs={
                "placeholder": "Introduce el número de teléfono",
                "maxlength": 9,
            }),
            "fecha_nacimiento": forms.DateInput(attrs={
                "type": "date",
            }),
        }

    

    def clean(self):
        cleaned_data = super().clean()

        telefono = cleaned_data.get('telefono')
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')

        # Validar que el teléfono tenga exactamente 9 dígitos
        if telefono:
            telefonostr = str(telefono)
            if len(telefonostr) != 9 or not telefonostr.isdigit(): # es para que no pueda introducir menos de 9 cifras (999999999)
                self.add_error('telefono', "El número de teléfono debe tener exactamente 9 dígitos y contener solo números.")
        else:
            self.add_error('telefono', "El número de teléfono es obligatorio.")

        # Validar que la fecha de nacimiento no sea nula
        if not fecha_nacimiento:
            raise forms.ValidationError("La fecha de nacimiento es obligatoria.")

        # Validar que la fecha de nacimiento no sea más de 100 años en el pasado
        hoy = date.today()
        anios_diferencia = hoy.year - fecha_nacimiento.year

        if anios_diferencia > 100:
            raise forms.ValidationError("El año de nacimiento no puede ser mayor a 100 años en el pasado.")

        # Validar que la fecha de nacimiento no sea futura
        if fecha_nacimiento > hoy:
            raise forms.ValidationError("La fecha de nacimiento no puede ser una fecha futura.")

        return cleaned_data

class BusquedaAvanzadaPasajero(forms.Form):
    
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    apellido = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    telefono = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )

    def clean(self):
        super().clean()

        nombre = self.cleaned_data.get('nombre')
        telefono = self.cleaned_data.get('telefono')


        if(nombre == ""):
                self.add_error("nombre","El nombre del aeropuerto no puede estar vacio")

        if telefono:  # Asegurarse de que el teléfono no sea None
            telefono_str = str(telefono)  # Convertir a cadena para verificar la longitud
            if len(telefono_str) != 9 or not telefono_str.isdigit():  # Verificar que tenga exactamente 9 dígitos y sea numérico
                self.add_error("telefono", "El número de teléfono debe tener exactamente 9 dígitos.")
        else:
            self.add_error("telefono", "Debe proporcionar un número de teléfono.")



        return self.cleaned_data