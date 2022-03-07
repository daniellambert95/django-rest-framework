from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    chapters = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    pages = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    class Condition(models.IntegerChoices):
        NEW = 1, "NEW"
        USED = 2, "USED"
        OLD = 3, "OLD"

    model = models.CharField(max_length=50)
    year = models.IntegerField()
    condition = models.PositiveSmallIntegerField(
                choices=Condition.choices,
                default=Condition.OLD
                )
    
    def __str__(self):
        return self.model