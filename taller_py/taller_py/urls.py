<<<<<<< HEAD
"""
documentacion de la aplicacion esto se puede borrar
URL configuration for taller_py project.
=======
>>>>>>> master

from django.contrib import admin
from django.urls import path
from App1.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView)
]
