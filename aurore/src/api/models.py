from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Alarm(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hour = models.TimeField()
    duration = models.PositiveSmallIntegerField(validators=[MaxValueValidator(20), MinValueValidator(1)])
    days = models.CharField(max_length=20, unique=True)
    status = models.BooleanField()

    def __str__(self):
        return '%s : %s on days %s' % (self.name, self.hour, self.days)

class Color(models.Model):
    color = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return '%s' % (self.color)