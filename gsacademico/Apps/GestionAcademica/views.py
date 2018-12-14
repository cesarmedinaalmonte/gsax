from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Nivel
from . models import Curso
from . models import Seccion
from . models import Materia
from . models import Docente
from . models import Curso
from . models import Estudiante
from . serializers import CursoSerializer
from . serializers import NivelSerializer
from . serializers import SeccionSerializer
from . serializers import MateriaSerializer
from . serializers import DocenteSerializer
from . serializers import EstudianteSerializer






# Create your views here.
class NivelList (APIView):

    def get(self, request):
        nivel = Nivel.objects.all()
        serializer =NivelSerializer(nivel, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class CursoList (APIView):

    def get(self, request):
        curso = Curso.objects.all()
        serializer =CursoSerializer(curso, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class SeccionList (APIView):

    def get(self, request):
        seccion = Seccion.objects.all()
        serializer =SeccionSerializer(seccion, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MateriaList (APIView):

    def get(self, request):
        materia = Materia.objects.all()
        serializer =MateriaSerializer(materia, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class DocenteList (APIView):

    def get(self, request):
        docente = Docente.objects.all()
        serializer = DocenteSerializer(docente, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class EstudianteList (APIView):

    def get(self, request):
        estudiante = Docente.objects.all()
        serializer = EstudianteSerializer(estudiante, many=True)
        return Response(serializer.data)

    def post(self):
        pass

