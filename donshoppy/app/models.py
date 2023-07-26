from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)
    contact=models.IntegerField()
    numerodpto=models.IntegerField()

    def __str__(self):
        return self.nombre

class Zapatilla(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

class Ropa(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)


    def __str__(self):
        return self.nombre
    
class Abarrote(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)


    def __str__(self):
        return self.nombre
    
class Herramienta(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)


    def __str__(self):
        return self.nombre

class Outdoor(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)


    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)


    def __str__(self):
        return self.nombre
    
class Mochila(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to="productos",null=True)


    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    comentario=models.TextField()

    def __str__(self):
        return self.nombre