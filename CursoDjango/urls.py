"""
URL configuration for CursoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from contenido import views
from django.conf import settings
from django.conf.urls.static import static
from cursos.views import (
    CursoListView, 
    CursoCreateView, 
    CursoUpdateView, 
    CursoDeleteView, 
    CursoDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('contacto/', views.contacto, name='contacto'),
    path('cursos/', views.cursos, name='cursos'),
    path('crud/', CursoListView.as_view(), name='lista_cursos_crud'),
    path('crud/nuevo/', CursoCreateView.as_view(), name='crear_curso'),
    path('crud/<int:pk>/', CursoDetailView.as_view(), name='detalle_curso'),
    path('crud/<int:pk>/editar/', CursoUpdateView.as_view(), name='editar_curso'),
    path('crud/<int:pk>/eliminar/', CursoDeleteView.as_view(), name='eliminar_curso'),
] 

if settings.DEBUG:

    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

