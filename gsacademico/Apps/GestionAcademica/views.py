from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from . models import Pariente
from . models import Materia
from . models import Docente
from . models import Curso
from . models import Estudiante
from . models import CursoMateria
from . models import Periodo
from . models import Inscripcion
from .serializers import CursoSerializer, PeriodoSerializer
from . serializers import MateriaSerializer
from . serializers import DocenteSerializer
from . serializers import EstudianteSerializer
from . serializers import ParienteSerializer
from . serializers import CursoMateriaSerializer
from . serializers import InscripcionSerializer
import django_filters

#Clase de paginación personalizada

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


# Create your views here.

class CursoList(viewsets.ModelViewSet):
        queryset = Curso.objects.all().order_by('nivel','nombre')
        serializer_class = CursoSerializer


class CursoListilimitada(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('nivel', 'nombre')
    serializer_class = CursoSerializer
    pagination_class = LargeResultsSetPagination

class MateriaList(viewsets.ModelViewSet):
        queryset = Materia.objects.all().order_by('nombre')
        serializer_class = MateriaSerializer
        filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class EstudianteList(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all().order_by('nombre')
    serializer_class = EstudianteSerializer
    filter_fields = ('nombre', 'id')


class Docentelist(viewsets.ModelViewSet):
        queryset = Docente.objects.all().order_by('nombre')
        serializer_class = DocenteSerializer


class Docentelistilimitada(viewsets.ModelViewSet):
    queryset = Docente.objects.all().order_by('nombre')
    serializer_class = DocenteSerializer
    pagination_class = LargeResultsSetPagination

class ParienteList(viewsets.ModelViewSet):
        queryset = Pariente.objects.all()
        serializer_class = ParienteSerializer


class CursoMateriaList(viewsets.ModelViewSet):
        queryset = CursoMateria.objects.all()
        serializer_class = CursoMateriaSerializer




class InscripcionList(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer


#Filtro
class PeriodoList(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

    class EstudianteFilter(django_filters.FilterSet):
        name = django_filters.CharFilter(lookup_expr='iexact')

        class Meta:
            model = Estudiante
            fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno' ]