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


class Nivel (models.Model):

    nombre = models.CharField(max_length=35)
    def __str__(self):
        return "{0}".format(self.nombre)

class Seccion (models.Model):

    nombre = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre

class Curso (models.Model):

    nivel = models.ForeignKey(Nivel, related_name='nivel',on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, related_name='seccion',  on_delete=models.CASCADE)
    grado = models.CharField(max_length=50)


    def __str__(self):
        return "{0} {1} {2}".format(self.grado,self.seccion, self.nivel)

    def nivelnombre(self):
        return self.nivel.nombre

    def seccionnombre(self):
        return self.seccion.nombre


class Materia (models.Model):

    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=8)


    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Codigo)

class CursoMateria (models.Model):

        idmateria = models.ForeignKey(Materia,null=False,blank=False, on_delete=models.CASCADE)
        idcurso = models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
        iddocente = models.ForeignKey(Docente,null=False,blank=False,on_delete=models.CASCADE)


class Periodo (models.Model):

        descripcion = models.CharField(max_length=16)
        estado = models.BooleanField(default=False)
        def __str__(self):
            return self.descripcion

class Inscripcion (models.Model):

        estudiante = models.ForeignKey(Estudiante, null=False, blank= False,on_delete= models.CASCADE)
        periodo = models.ForeignKey(Periodo, null=False, blank=False, on_delete= models.CASCADE)
        cursoMateria = models.ForeignKey(CursoMateria,null=True, blank=True, on_delete= models.CASCADE)


