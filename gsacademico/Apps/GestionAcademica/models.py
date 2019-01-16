from django.db import models

# Create your models here.



class Docente (models.Model):

    apellido = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    SEXO = (('M', 'Masculino' ), ('F','Femenino'))
    sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    telefono = models.CharField(null=True,blank=True,max_length=10)
    email = models.EmailField(null=True,blank=True,max_length=60)
    direccion =  models.CharField(max_length=120)

    def NombreCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.apellido, self.nombre)
    def __str__(self):
        return self.NombreCompleto()

class Pariente (models.Model):

    apellido = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    SEXO = (('M', 'Masculino'), ('F', 'Femenino'))
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    telefono = models.CharField(null=True, blank=True, max_length=10)
    email = models.EmailField(null=True, blank=True, max_length=60)
    direccion = models.CharField(max_length=120)

    def NombreCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.apellido, self.nombre)

    def __str__(self):
        return self.NombreCompleto()

class Estudiante (models.Model):

    apellidoPaterno = models.CharField(max_length=60)
    apellidoMaterno = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    SEXO = (('M', 'Masculino' ), ('F','Femenino'))
    sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    fechaNacimiento = models.DateField()
    email =  models.EmailField(null=True,blank=True,max_length=60)
    padre = models.ForeignKey(Pariente,null=True,blank=True, on_delete=models.CASCADE)


    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)
    def __str__(self):
        return self.NombreCompleto()




class Curso (models.Model):

    SECCION = (('A','A'),('B','B'),('C','C'),('D','D'),('E','E'))
    NIVEL = (('Inicial','Inicial'),('Primaria','Primaria'),('Secundaria','Secundaria'))
    nivel = models.CharField(max_length=20,choices=NIVEL,default='Primaria')
    seccion = models.CharField(max_length=1,choices=SECCION,default='A')
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return "{0} {1} {2}".format(self.nombre,self.seccion, self.nivel)



class Materia (models.Model):

    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=8)


    def __str__(self):
        return "{0} ({1})".format(self.nombre, self.codigo)

class CursoMateria (models.Model):

        materia = models.ForeignKey(Materia,related_name='materia', on_delete=models.CASCADE)
        curso = models.ForeignKey(Curso,related_name='curso',on_delete=models.CASCADE)
        docente = models.ForeignKey(Docente,related_name='docente',on_delete=models.CASCADE)


class Periodo (models.Model):

        descripcion = models.CharField(max_length=16)
        estado = models.BooleanField(default=False)
        def __str__(self):
            return self.descripcion

class Inscripcion (models.Model):

        estudiante = models.ForeignKey(Estudiante, null=False, blank= False,on_delete= models.CASCADE)
        periodo = models.ForeignKey(Periodo, null=False, blank=False, on_delete= models.CASCADE)
        cursoMateria = models.ForeignKey(CursoMateria,null=True, blank=True, on_delete= models.CASCADE)


