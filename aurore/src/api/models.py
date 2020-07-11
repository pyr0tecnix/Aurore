from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from uuid import uuid1


class Alarm(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hour = models.TimeField()
    duration = models.PositiveSmallIntegerField(validators=[MaxValueValidator(20), MinValueValidator(1)])
    days = models.CharField(max_length=20)
    status = models.BooleanField()
    task_id = models.UUIDField(unique=True, default=uuid1)

    def __str__(self):
        return '%s : %s on days %s' % (self.name, self.hour, self.days)

class Color(models.Model):
    color = models.CharField(max_length=7, unique=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.color)

class Running(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')