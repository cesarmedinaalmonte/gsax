
from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers

from .models import Curso, Periodo
from  .models import  Materia
from  .models import  Nivel
from  .models import  Seccion
from  .models import  Estudiante
from  .models import  Docente
from  .models import Pariente
from  .models import  MateriaCurso




class NivelSerializer(ModelSerializer):


    class Meta:
        model = Nivel
        fields = ('id','Nombre')
    #        fields = ('Grado')

class SeccionSerializer(ModelSerializer):


    class Meta:
        model = Seccion
        fields = ('id','Nombre')
    #        fields = ('Grado')

class CursoSerializer(ModelSerializer):

    #nivel = NivelSerializer(many=True, read_only= True)
    seccion = SeccionSerializer(many=False, read_only=True)

    class Meta:
        model = Curso
        fields = ('id','seccion')
         #        fields = ('Grado')


class MateriaSerializer(ModelSerializer):

    class Meta:
        model = Materia
        fields = ( 'id','Nombre', 'Codigo')
    #        fields = ('Grado')

class EstudianteSerializer(ModelSerializer):

    class Meta:
        model = Estudiante
        fields = ('__all__')
    #        fields = ('Grado')




class DocenteSerializer(ModelSerializer):

    class Meta:
        model = Docente
        fields = ('__all__')
    #        fields = ('Grado')

class ParienteSerializer(ModelSerializer):

    class Meta:
        model = Pariente
        fields = ('__all__')
    #        fields = ('Grado')

class MateriaCursoSerializer(ModelSerializer):

    class Meta:
        model = MateriaCurso
        fields = ('id','idmateria', 'idcurso', 'idseccion','iddocente' )
    #        fields = ('Grado')



class PeriodoSerializer(ModelSerializer):

    class Meta:
        model = Periodo
        fields = ('id','descripcion','estado')
    #        fields = ('Grado')