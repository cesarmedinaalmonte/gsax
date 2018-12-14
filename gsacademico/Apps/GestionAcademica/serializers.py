from rest_framework import serializers

from .models import Curso
from  .models import  Materia
from  .models import  Nivel
from  .models import  Seccion
from  .models import  Estudiante
from  .models import  Docente
from  .models import Pariente




class NivelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel
        fields = ('__all__')
    #        fields = ('Grado')

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ('__all__')
#        fields = ('Grado')

class SeccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seccion
        fields = ('__all__')
    #        fields = ('Grado')

class MateriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materia
        fields = ('__all__')
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




