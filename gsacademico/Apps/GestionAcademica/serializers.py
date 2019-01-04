
from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers

from .models import Curso, Periodo
from  .models import  Materia
from  .models import  Nivel
from  .models import  Seccion
from  .models import  Estudiante
from  .models import  Docente
from  .models import Pariente
from  .models import  CursoMateria
from  .models import  Inscripcion




class NivelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Nivel
        fields = [
            'id',
            'nombre'
        ]
    #        fields = ('Grado')

class SeccionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Seccion
        fields = [
            'id',
            'nombre'
        ]



class CursoSerializer(serializers.ModelSerializer):

    seccion = SeccionSerializer(many=False, read_only=True)
    nivel = NivelSerializer(many= False, read_only= True)
    class Meta:
        model = Curso
        fields = [
            'id',
            'nivel',
            'seccion',
            'grado'
        ]


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

    idmateria = MateriaSerializer(many=False , read_only=True)
    idcurso = CursoSerializer(many= False , read_only= True)
    iddocente = DocenteSerializer(many=False, read_only=True)
    class Meta:
        model = CursoMateria
        fields = [
            'id',
            'idmateria',
            'idcurso',
            'iddocente'
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