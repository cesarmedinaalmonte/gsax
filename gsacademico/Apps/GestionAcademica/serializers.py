
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
    padre = serializers.StringRelatedField(many=False)

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


class CursoMateriaSerializer(serializers.ModelSerializer):

    # materia = MateriaSerializer()
    # curso = CursoSerializer(many=False, read_only=True)
    # docente = DocenteSerializer(many=False, read_only=True)

    # materia = Materia.objects.filter(pk=2) # matetica

    # print('test',materia_queryset)
    # exit()

    # materia = Materia.objects.all()

    # materia = serializers.PrimaryKeyRelatedField(queryset=Materia.objects.all())
    # curso = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all())
    # docente = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all())

    class Meta:
        model = CursoMateria
        fields = ( 'id', 'materia', 'curso', 'docente')


class PeriodoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Periodo
        fields = [
            'id',
            'descripcion',
            'estado'
        ]
class InscripcionSerializer(serializers.ModelSerializer):


    estudiante = serializers.PrimaryKeyRelatedField(many= False , read_only=True)
    periodo = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    cursoMateria = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Inscripcion
        fields = [
            'id',
            'estudiante',
            'periodo',
            'cursoMateria'
        ]