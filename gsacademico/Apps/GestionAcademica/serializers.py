from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


from .models import Curso, Periodo
from  .models import  Materia
from  .models import  Nivel
from  .models import  Seccion
from  .models import  Estudiante
from  .models import  Docente
from  .models import Pariente
from  .models import  MateriaCurso




class NivelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel
        fields = ('id','Nombre')
    #        fields = ('Grado')

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ('id','Nivel','Grado','Seccion')
         #        fields = ('Grado')

class SeccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seccion
        fields = ('id''nombre')
    #        fields = ('Grado')

class MateriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materia
        fields = ( 'id','Nombre', 'Codigo', 'Profesor')
    #        fields = ('Grado')

class EstudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudiante
        fields = ('__all__')
    #        fields = ('Grado')




class DocenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Docente
        fields = ('__all__')
    #        fields = ('Grado')

class ParienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pariente
        fields = ('__all__')
    #        fields = ('Grado')

class MateriaCursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MateriaCurso
        fields = ('id','idmateria', 'idcurso', 'idseccion','iddocente' )
    #        fields = ('Grado')



class PeriodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Periodo
        fields = ('id','descripcion','estado')
    #        fields = ('Grado')