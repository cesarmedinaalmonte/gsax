from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from . models import Nivel
from . models import Pariente
from . models import Seccion
from . models import Materia
from . models import Docente
from . models import Curso
from . models import Estudiante
from . models import CursoMateria
from . models import Periodo
from . models import Inscripcion
from .serializers import CursoSerializer, PeriodoSerializer
from . serializers import NivelSerializer
from . serializers import SeccionSerializer
from . serializers import MateriaSerializer
from . serializers import DocenteSerializer
from . serializers import EstudianteSerializer
from . serializers import ParienteSerializer
from . serializers import CursoMateriaSerializer
from . serializers import InscripcionSerializer

import django_filters


# Create your views here.
class NivelList (viewsets.ModelViewSet):
        queryset = Nivel.objects.all()
        serializer_class =  NivelSerializer


class CursoList(viewsets.ModelViewSet):
        queryset = Curso.objects.all()
        serializer_class = CursoSerializer


class SeccionList(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class MateriaList(viewsets.ModelViewSet):
        queryset = Materia.objects.all()
        serializer_class = MateriaSerializer


class EstudianteList(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class Docentelist(viewsets.ModelViewSet):
        queryset = Docente.objects.all()
        serializer_class = DocenteSerializer


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
            fields = ['Nombre', 'ApellidoPaterno', 'ApellidoMaterno' ]