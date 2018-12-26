from django.db import models

# Create your models here.



class Docente (models.Model):

    ApellidoPaterno = models.CharField(max_length=60)
    ApellidoMaterno = models.CharField(max_length=60)
    Nombre = models.CharField(max_length=60)
    SEXO = (('M', 'Masculino' ), ('F','Femenino'))
    Sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    FechaNacimiento = models.DateField()
    TelefonoCasa = models.CharField(max_length=10)
    TelefonoCelular = models.CharField(max_length=10)
    CorreoEmpresarial =  models.EmailField(max_length=60)
    CorreoPersonal =  models.EmailField(max_length=60)
    Direccion =  models.CharField(max_length=120)

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombre)
    def __str__(self):
        return self.NombreCompleto()

class Pariente (models.Model):

    ApellidoPaterno = models.CharField(max_length=60)
    ApellidoMaterno = models.CharField(max_length=60)
    Nombre = models.CharField(max_length=60)
    SEXO = (('M', 'Masculino' ), ('F','Femenino'))
    Sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    FechaNacimiento = models.DateField()
    TelefonoCasa = models.CharField(max_length=10)
    TelefonoCelular = models.CharField(max_length=10)
    CorreoEmpresarial =  models.EmailField(max_length=60)
    CorreoPersonal =  models.EmailField(max_length=60)
    Direccion =  models.CharField(max_length=120)

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombre)
    def __str__(self):
        return self.NombreCompleto()

class Estudiante (models.Model):

    ApellidoPaterno = models.CharField(max_length=60)
    ApellidoMaterno = models.CharField(max_length=60)
    Nombre = models.CharField(max_length=60)
    SEXO = (('M', 'Masculino' ), ('F','Femenino'))
    Sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    FechaNacimiento = models.DateField()
    CorreoPersonal =  models.EmailField(max_length=60)
    PADRE = models.ForeignKey(Pariente,null=True,blank=True, on_delete=models.CASCADE)


    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombre)
    def __str__(self):
        return self.NombreCompleto()


class Nivel (models.Model):

    Nombre = models.CharField(max_length=35)
    def __str__(self):
        return "{0}".format(self.Nombre)

class Seccion (models.Model):

    Nombre = models.CharField(max_length=1)

    def __str__(self):
        return "{0}".format(self.Nombre)

class Curso (models.Model):

    Nivel = models.ForeignKey(Nivel,null=False,blank=False,on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion,null=True,blank=True, on_delete=models.CASCADE)
    Grado = models.CharField(max_length=50)
    Titular = models.ForeignKey(Docente, null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1} {2}".format(self.Grado,self.Seccion, self.Nivel)

    def Nivelnombre(self):
        return self.Nivel.Nombre

    def Seccionnombre(self):
        return self.Seccion.Nombre


class Materia (models.Model):

    Nombre = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=8)


    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Codigo)

class MateriaCurso (models.Model):

        idmateria = models.ForeignKey(Materia,null=False,blank=False, on_delete=models.CASCADE)
        idcurso = models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
        iddocente = models.ForeignKey(Docente,null=False,blank=False,on_delete=models.CASCADE)


class Periodo (models.Model):

        descripcion = models.CharField(max_length=16)
        estado = models.BooleanField(default=False)
        def __str__(self):
            return self.descripcion

class Inscripcion (models.Model):

        Estudiante = models.ForeignKey(Estudiante, null=False, blank= False,on_delete= models.CASCADE)
        Periodo = models.ForeignKey(Periodo, null=False, blank=False, on_delete= models.CASCADE)

