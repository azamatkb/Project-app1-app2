from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Cars(models.Model):
    car = models.CharField("Марка", max_length=150)
    color = models.CharField("Цвет", max_length=150)
    enginvol = models.FloatField("Объем двигателя",) 
    transmission = models.CharField("Коробка передач", max_length=150)
    oil = models.CharField("Вид топлива", max_length=150)

    def __str__(self):
        return f"{self.car}, {self.color}, {self.enginvol}, {self.transmission}, {self.oil}"

class Meta:
    verbose_name = "Машина"
    verbose_name_plural = "Машины"

