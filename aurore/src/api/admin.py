from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Alarm)
admin.site.register(models.Color)
admin.site.register(models.Running)
