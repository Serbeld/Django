"""CursoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from CursoDjango.FirstPage import hello, hide, fecha_h, tu_edad, autor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('hide/', hide),
    path('date/', fecha_h),
    path('autor/', autor),
    path('Tuedad/<int:edad>/<int:agno>', tu_edad)
]
