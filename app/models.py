from django.db import models
from django.conf import settings

class Cliente (models.Model):
    nombre = models.CharField( max_length=50)
    direccion = models.CharField( max_length=50)
    ciudad = models.CharField( max_length=50)
    comuna = models.CharField( max_length=50)
    telefono = models.CharField( max_length=15)
    correo = models.EmailField(max_length = 50)
    tecnico = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__ (self):
        return self.nombre

#class Tecnico (models.Model):
#    nombre = models.CharField( max_length=50)
#    correo = models.EmailField(max_length = 50, unique=True)

#    def __str__ (self):
#        return self.nombre



class OrdenTrabajo (models.Model):
    folio = models.AutoField(primary_key=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    tecnico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora_inicio = models.DateTimeField( auto_now=False, auto_now_add=False)
    hora_termino = models.DateTimeField( auto_now=False, auto_now_add=False)
    nom_cliente = models.CharField(max_length=50)


    def __str__ (self):
        return str(self.folio)


class Ascensor(models.Model):
    modelo = models.CharField( max_length=50)

    def __str__ (self):
        return self.modelo

class Detalle_Orden (models.Model):
    folio = models.ForeignKey("OrdenTrabajo", on_delete=models.CASCADE)
    fallas_detectadas = models.TextField(max_length=1000)
    reparaciones_efectuadas = models.TextField(max_length=1000)
    piezas_cambiadas = models.TextField(max_length=1000)
    ascensor = models.ForeignKey("Ascensor", on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.folio)


