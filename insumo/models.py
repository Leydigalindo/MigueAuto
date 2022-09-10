from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=45)
    
    def __str__(self):
        return f'{self.nombre}'  


class Insumo(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    marca =  models.ForeignKey(Marca,on_delete=models.CASCADE ,related_name="insumos_db")   
    def __str__(self):
        return f'{self.nombre}, {self.marca}' 
    
class Servicio(models.Model):
    valor = models.IntegerField()
    def str(self):
        return self.valor
    
        