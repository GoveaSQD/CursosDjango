from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Curso
from django.contrib import messages

class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/lista_cursos_crud.html'
    context_object_name = 'cursos'
    
    def get_queryset(self):
        return Curso.objects.filter(activo=True)

class CursoCreateView(CreateView):
    model = Curso
    template_name = 'cursos/curso_form.html'
    fields = ['nombre', 'descripcion', 'duracion', 'turno', 'cupo', 'precio', 'activo', 'imagen']
    success_url = reverse_lazy('lista_cursos_crud')
    
    def form_valid(self, form):
        messages.success(self.request, 'Curso creado exitosamente!')
        return super().form_valid(form)

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'cursos/curso_form.html'
    fields = ['nombre', 'descripcion', 'duracion', 'turno', 'cupo', 'precio', 'activo', 'imagen']
    success_url = reverse_lazy('lista_cursos_crud')
    
    def form_valid(self, form):
        messages.success(self.request, 'Curso actualizado exitosamente!')
        return super().form_valid(form)

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('lista_cursos_crud')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Curso eliminado exitosamente!')
        return super().delete(request, *args, **kwargs)

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/curso_detalle.html'