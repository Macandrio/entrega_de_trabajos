from django.urls import path
from django.conf.urls import handler404, handler500, handler403, handler400

from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path("usuario/", views.lista_usuario,name="lista_usuario"),


    path("proyecto/", views.dame_proyecto,name="dame_proyecto"),
    path('proyectos/<int:proyecto_id>/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),  # Tareas por proyecto
    path('usuario/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),  # Usuarios tarea asignadas
    path('asignaciones/<int:tarea_id>/', views.asignacion_tarea, name='asignacion_tarea'),  # URL para obtener asignaciones por tarea
    path("asignaciones/<str:texto_observaciones>/tarea", views.texto_observaciones,name="texto_observaciones"),
    path("tarea/proyecto/<int:fecha_inicio>/<int:fecha_final>", views.tarea_completada,name="tarea_completada"),
    path('tarea/<int:tarea_id>/comentarios/<str:palabra>/<int:anio>/', views.comentarios_por_palabra_y_anio, name='comentarios_por_palabra_y_anio'),
    path('proyecto/<int:proyecto_id>/etiquetas/', views.etiquetas_por_proyecto, name='etiquetas_por_proyecto'),
    #path('usuarios/no-asignados/', views.usuarios_no_asignados, name='usuarios_no_asignados'),

    path('operadores/', views.mostrar_operadores, name='mostrar_operadores'),


]

# Manejar errores
handler404 = 'ejercicio.views.handler_404'
handler500 = 'ejercicio.views.handler_500'
handler403 = 'ejercicio.views.handler_403'
handler400 = 'ejercicio.views.handler_400'