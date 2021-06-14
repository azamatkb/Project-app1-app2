from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Renthouse(models.Model):
    country = models.CharField("Страна", max_length=150)
    flour = models.IntegerField("Этаж",)
    numroom = models.IntegerField("Кол-во комнат",) 
    numdays = models.IntegerField("Кол-во дней",)
    cost = models.IntegerField("Стоимость",)

    def __str__(self):
        return f"{self.country}, {self.flour}, {self.numroom}, {self.numdays}, {self.cost}"