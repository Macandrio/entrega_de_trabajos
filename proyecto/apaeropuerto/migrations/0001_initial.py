# Generated by Django 5.1.2 on 2024-10-17 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aerolinea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
                ('pais', models.CharField(max_length=100)),
                ('fecha_fundacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('codigo_iata', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField()),
                ('aeropuerto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Equipaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('dimensiones', models.CharField(max_length=50)),
                ('tipo_material', models.CharField(max_length=30)),
                ('pasajero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.pasajero')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.IntegerField()),
                ('distancia', models.FloatField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas_destino', to='apaeropuerto.aeropuerto')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas_origen', to='apaeropuerto.aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(max_length=100)),
                ('costo', models.FloatField()),
                ('duracion', models.IntegerField()),
                ('aeropuerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_vuelo', models.CharField(max_length=10)),
                ('hora_salida', models.DateTimeField()),
                ('hora_llegada', models.DateTimeField()),
                ('estado', models.CharField(max_length=20)),
                ('aeropuerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Silla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('clase', models.CharField(max_length=20)),
                ('precio', models.FloatField()),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.vuelo')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField()),
                ('estado', models.CharField(max_length=50)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.pasajero')),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.vuelo')),
            ],
        ),
        migrations.CreateModel(
            name='VueloAerolinea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_operacion', models.DateTimeField()),
                ('estado', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('aerolinea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.aerolinea')),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apaeropuerto.vuelo')),
            ],
        ),
    ]