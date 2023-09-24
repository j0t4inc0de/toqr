"""
URL configuration for toqr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import procesar_datos
from app.views import inicio, procesar_datos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('https://j0t4inc0de.github.io/tuqr/', inicio),
    path('https://j0t4inc0de.github.io/tuqr/qr/', procesar_datos, name='procesar_datos')
]