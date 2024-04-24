from django.db import models

class AutorDb(models.Model):
    Nombre = models.CharField(max_length=75, verbose_name="Nombre")
    Fecha_nacimiento = models.DateField(verbose_name="Fecha nacimiento", null=False, blank=False)
    Fecha_fallecimiento = models.DateField(verbose_name="Fecha fallecimiento", null=True, blank=True)
    Profesion = models.CharField(max_length=50, verbose_name="Profesion")
    Nacionalidad = models.CharField(max_length=50, verbose_name="Nacionalidad")

    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return self.Nombre

class FraseDb(models.Model):
    Cita = models.TextField(max_length=400, verbose_name="Cita")
    Autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"
        
   