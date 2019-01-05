
from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers, status

from .models import Curso, Periodo
from  .models import  Materia
from  .models import  Estudiante
from  .models import  Docente
from  .models import Pariente
from  .models import  CursoMateria
from  .models import  Inscripcion





class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = [
            'id',
            'nombre',
            'seccion',
            'nivel'
        ]
        def create(self, validated_data):
            seccion_data = validated_data.pop('seccion')
            curso = Curso.objects.create(validated_data)
            return curso


class MateriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materia
        fields = [
            'id',
            'nombre',
            'codigo'
    ]

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

class CursoMateriaSerializer(serializers.ModelSerializer):

    materia = MateriaSerializer(many=False , read_only=True)
    curso = CursoSerializer(many= False , read_only= True)
    docente = DocenteSerializer(many=False, read_only=True)
    class Meta:
        model = CursoMateria
        fields = [
            'id',
            'materia',
            'curso',
            'docente'
        ]


class PeriodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Periodo
        fields = [
            'id',
            'descripcion',
            'estado'
        ]
class InscripcionSerializer(serializers.ModelSerializer):

    estudiante = EstudianteSerializer(many= False , read_only=False)
    periodo = PeriodoSerializer(many= False, read_only=False)
    cursoMateria = CursoMateriaSerializer(many=False, read_only=False)

    class Meta:
        model = Inscripcion
        fields = [
            'id',
            'estudiante',
            'periodo',
            'cursoMateria'
        ]