from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("__debug__/", include("debug_toolbar.urls")),
]