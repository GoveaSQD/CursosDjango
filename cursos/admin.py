from django.contrib import admin
from .models import Alumnos, Comentario, Curso  # Importación única

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'correo', 'curso', 'turno', 'created', 'updated')
    search_fields = ('nombre', 'correo', 'curso')
    list_filter = ('curso', 'turno', 'created')
    date_hierarchy = 'created'
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'correo', 'curso', 'turno', 'imagen')
        }),
        ('Fechas', {
            'fields': ('created', 'updated')
        }),
    )

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'created')
    search_fields = ('id', 'alumno__nombre', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

class AdministrarCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'duracion', 'cupo', 'precio', 'activo', 'created', 'updated')
    search_fields = ('nombre', 'descripcion', 'duracion')
    list_filter = ('activo', 'created')
    date_hierarchy = 'created'
    fieldsets = (
        ('Datos del Curso', {
            'fields': ('nombre', 'descripcion', 'duracion', 'cupo', 'precio', 'activo', 'imagen')
        }),
        ('Fechas', {
            'fields': ('created', 'updated')
        }),
    )

# Configuración del admin
admin.site.site_header = "CONVOCATORIAS"
admin.site.site_title = "CONVOCATORIAS"
admin.site.index_title = "Cursos"

# Registro de modelos (solo una vez)
admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Comentario, AdministrarComentarios)
admin.site.register(Curso, AdministrarCursos)