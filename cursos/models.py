from django.db import models
from ckeditor.fields import RichTextField

class Alumnos(models.Model):
    CURSO_CHOICES = [
        ('Python', 'Python'),
        ('Base de Datos', 'Base de Datos'),
        ('JavaScript', 'JavaScript'),
        ('POO', 'POO'),
        ('MongoDB', 'MongoDB'),
    ]
    TURNO_CHOICES = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino')
    ]

    nombre = models.TextField()
    correo = models.EmailField(verbose_name='Correo electrónico', null=True, blank=True)
    curso = models.CharField(max_length=20, choices=CURSO_CHOICES, verbose_name='Curso', default='Python')  
    turno = models.CharField(max_length=20, choices=TURNO_CHOICES,)
    imagen = models.ImageField(null=True, upload_to="fotos")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['-created']

    def __str__(self):
        return self.nombre
# Create your models here.

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    coment = RichTextField(verbose_name='Comentario', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta: 
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.alumno} - {self.coment[:30] if self.coment else ''}"
    
class Curso(models.Model):
    CURSO_CHOICES = [
        ('Python', 'Python'),
        ('Base de Datos', 'Base de Datos'),
        ('JavaScript', 'JavaScript'),
        ('POO', 'POO'),
        ('MongoDB', 'MongoDB'),
    ]
    TURNO_CHOICES = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino')
    ]

    nombre = models.CharField(max_length=20, choices=CURSO_CHOICES, verbose_name='Nombre del curso', default='Python')  
    descripcion = models.TextField(verbose_name="Descripción")      
    duracion = models.CharField(max_length=50, verbose_name="Duración (Horas)", null=True, blank=True)
    turno = models.CharField(max_length=20, choices=TURNO_CHOICES, null=True, blank=True, verbose_name="Turno")
    cupo = models.IntegerField(verbose_name="Cupo máximo")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio (pesos)") 
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")
    imagen = models.ImageField(upload_to="fotos", null=True, blank=True, verbose_name="Imagen del curso") 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de inicio")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['created']

    def __str__(self):
        return self.nombre