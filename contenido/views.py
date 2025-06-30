from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'contenido/pagina_principal.html')


def contacto(request):
    return render(request, 'contenido/contacto.html')

def cursos(request):
    return render(request, 'contenido/cursos.html')