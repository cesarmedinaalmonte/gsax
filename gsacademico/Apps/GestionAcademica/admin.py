from django.contrib import admin
from gsacademico.Apps.GestionAcademica.models import *


# Register your models here.

admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Docente)
admin.site.register(Pariente)
admin.site.register(Estudiante)
admin.site.register(CursoMateria)
admin.site.register(Periodo)
admin.site.register(Inscripcion)


