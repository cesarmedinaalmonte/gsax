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


    def __str__(self):
        return "{0} {1} {2}".format(self.Grado,self.Seccion, self.Nivel)



class Materia (models.Model):

    Nombre = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=8)
    Profesor = models.ManyToManyField(Docente)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Codigo)
