
from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers, status

from .models import Curso, Periodo
from  .models import  Materia
from  .models import  Estudiante
from  .models import  Docente
from  .models import Pariente
from  .models import  CursoMateria
from  .models import  Inscripcion
from drf_writable_nested import WritableNestedModelSerializer

class CursoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Curso
        fields = [
            'id',
            'nombre',
            'seccion',
            'nivel'
        ]


class MateriaSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Materia
        fields = [
            'id',
            'nombre',
            'codigo'
    ]

class ParienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pariente
        fields = ('__all__')
    #        fields = ('Grado')

class EstudianteSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    padre = ParienteSerializer()

    class Meta:
        model = Estudiante
        fields = (
            'id',
            'apellidoPaterno',
            'apellidoMaterno',
            'nombre','sexo',
            'fechaNacimiento',
            'email',
            'padre'
        )

class DocenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Docente
        fields = ('__all__')
    #        fields = ('Grado')


class CursoMateriaSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):

    materia = MateriaSerializer(many=False, required=True)
    curso = CursoSerializer(many= False, required=True)
    docente = DocenteSerializer(many=False, required=True)


    class Meta:
        model = CursoMateria
        fields = [
            'id',
            'materia',
            'curso',
            'docente'
        ]

class PeriodoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Periodo
        fields = [
            'id',
            'descripcion',
            'estado'
        ]
class InscripcionSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):


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