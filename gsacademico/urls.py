"""gsacademico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path , include
from rest_framework import urls , routers
from rest_framework.urlpatterns import format_suffix_patterns
from gsacademico.Apps.GestionAcademica.views import NivelList,CursoList, \
    SeccionList, MateriaList, EstudianteList, Docentelist, ParienteList, PeriodoList, CursoMateriaList, InscripcionList

apiurl = routers.SimpleRouter()

apiurl.register('nivel', NivelList )
apiurl.register('curso', CursoList )
apiurl.register('seccion', SeccionList )
apiurl.register('materia', MateriaList )
apiurl.register('estudiante', EstudianteList )
apiurl.register('docente', Docentelist )
apiurl.register('pariente', ParienteList )
apiurl.register('periodo', PeriodoList )
apiurl.register('cursomateria', CursoMateriaList )
apiurl.register('inscripcion', InscripcionList )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apiurl.urls))

]
