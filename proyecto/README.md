# entrega_de_trabajos
Mi pagina web va a consistir en un Aeropuerto en general con sus aerolineas que serian las distintas empresa como rayane, vueling ... ,
los vuelos que hay con sus pasajeros que seran las personas , los trabajadores que trabajen en el aeropuerto , el equipage que lleve una persona tambien las reservas de las personas , las ruta que deben tomar los aviones, y lod sitios del avion donde se sienta la gente.

sera una pagina donde se controlara toda la informacion de un aeropuerto 
-------------------------------------------------------------------------------------------------------------------------------------------
Aeropuerto
    Atributos: 4
        Nombre (varchar ,maximo de caracteres 2, choices para que solo pueda elegir entre varios nombres , por defecto que ponga ES)
        Ciudad (varchar ,maximo de caracteres 2, choices para que solo pueda elegir entre varias ciudades , por defecto que ponga ES)
        País (varchar , maximo de caracteres 2, choices para que solo pueda elegir entre varios paises , por defecto que ponga ES)
        capacidad maxima (Entero, este campo por defecto es 150)

Vuelo
    Atributos: 5
        numero_vuelo_dia (Entero, nombra a la columna como veces_volado_dia, pone un error si se queda en blanco)
        hora_salida (dia y hora)
        hora_llegada (dia y hora)
        volando (si esta volando o no)
        duracion(duracion , no se puede editar)

        Relacion :1
            aeropuerto(Relacion Muchos a Uno) 

Pasajero
    Funcion:
        Valida si el dominio esta bien o no escrito y te pone un erro si no esta bien escrito

    Atributos: 5
        nombre (varchar,maximo 20 caracteres)
        apellido (varchar, maximo 20 caracteres, hacepta valores vacios)
        email (verifica el correo)
        telefono (Enteros , valida hasta 9 valores, puede ser un campo vacio)
        fecha de nacimiento (Dia y hora, puede ser nulo)

        Relacion:2
            aerouerto(relacion Muchos a Uno)

Equipage
    Atributos: 4
        peso (decimales)
        dimensiones (varchar)
        tipo de material (varchar)
        color (varchar)

        Relacion: 2
            pasajero (Relacion Uno a Uno)
            vuelo (Muchos a Uno)

Aerolinea
    Atributos: 4
        nombre (varchar de 100 caracterex max, nombre que mostrara en el formulario en vez de nombre aerolinea operadora)
        codigo (varchar, maximo 10 caracteres)
        fecha fundacion (dia y hora , guarda automaticamente la fecha y hora al crear un registro)
        pais (varchar, maximo 2 caracteres , chices para que elija uno de los paises proporcionados, por defecto sera españa)

        Relacion : 1
            aerolinea(muchos a muchos)

VueloAerolinea (Tabla intermedia)
    Atributos: 5
        id (clave foranea) atributo estra
        fecha operacion(dia y hora)
        esatdo (texto)
        clase(varchar , choices para elegir una clase)
        numero de aviones volando (Enteros,por defecto 5)

        Relaciones: 2
            vuelo(Muchos a Uno)
            aerolinea(Muchos a Uno)

Reserva
    Atributo
        fecha de la reserva (por defecto es la fechqa de creacion)
        estado (varchar maximo 50 caracteres, introduce una ayuda)
        metodo de pago (varchar, choise para elegir metodo, por defecto targeta)
        estado de pago (verdad o falso , por defecto falso)

        Relacion
            pasajero(ForeignKey ) relacion mucho a uno
            vuelo(ForeignKey) relacion mucho a uno

Empleado
    Atributo
        nombre (varchar, maximo 100 caracteres)
        apellido (varchar, maximo 100 caracteres)
        cargo (varchar,maximo 2 caracteres, choices para saber si es jefe o empleado)
        fecha_contratacion (dia y hora)

        Relacion
            aeropuerto (Muchos a Uno)
            vuelo (muchos a muchos)

Silla
    Atributos
        numero (Entero)
        clase (varchar , maximo 1 caracter, choices para elegir la clase y por defecto Economico)
        precio (decimales, ,maximo 5 digitos, 2 decimales)
        posicion (Enteros)

        Relacion
            vuelo (Muchos a Uno)
            pasajero(Uno a Uno)

Servicio
    Atributos
        tipo de servicio (varchar , maximo 100 caracter)
        costo (decimales)
        duracion del servicio (tiempo)
        añadido del servicio (varchar, maximo 100 caracter)

        Relacion
            aeropuerto (Uno a Uno)
            vuelo (Muchos a Uno)
            pasajeros (muchos a muchos)

Ruta
    Atributos
        salida (varchar de 100)
        destino (varchar de 100)
        duracion (tiempo)
        distancia (Decimal)

        Relacion
            aeropuerto (muchos a muchos)

-------------------------------------------------------------------------------------------------------------------
*    Definir en qué consistirá mi página Web

*    Crear repositorio Git de mi página Web

*    Preparar el proyecto Django con nuestra aplicación

*    Definir 10 modelos de mi página Web que cumpla los siguientes requisitos.Al menos 3 relaciones OneToOne, 3 relaciones ManytoOne, 3 relaciones       ManyToMany(Al menos una de ella debe tener una tabla intermedia con atributos extras)

*    Cada modelo debe tener al menos 4 campos.  Y debe exisitr en total 10 atributos de distinto tipo.No son válidos los atributos de relaciones.

*    Debe usasrse al menos 10 parámetros distinto entre todos los atributos creados de todos los modelos.

*    Crear el modelo entidad-relación de la base de datos.

*    En el README.MD debe especificarse en que consiste cada modelo, cada atributo y cada parámetro usado. Y el esquema de modelo entidad-relación.

*    Rellenar las tablas con seeders.

    Crear un backup de los datos con fixture.

*    No subir a git los archivos que no son necesarios que ya hemos explicado en clase

    Explicar cualquier código que no se haya visto en clase. Funciones, parámetros, etc..

    Debe entregarse el enlace de git.



comandos 

python manage.py migrate
python manage.py makemigrations apaeropuerto
python manage.py migrate apaeropuerto
python manage.py seed apaeropuerto --number=5

python manage.py createsuperuser
python manage.py runserver